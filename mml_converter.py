import re
import os
import requests
from urllib.parse import urljoin
import uuid
from colour import Color

# Global dictionaries to store variables, components, and hashmaps
variables = {}
components = {}
hashmaps = {}

# Shared contexts for components, variables, and hashmaps from included files
shared_components = {}
shared_variables = {}
shared_hashmaps = {}

# Syntax mapping for conversion
general_syntax_map = {
    r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)': r'<\1\2>',  # () -> <>
}

def process_native_include(match):
    filename = match.group(1).strip()
    raw_url = f'https://raw.githubusercontent.com/BridgerSilk/mml-lang/main/components/{filename}'
    
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        included_content = response.text
        # Recursively process includes inside the native component
        included_content = extract_includes(included_content)
        included_content = extract_variables(included_content)
        included_content = assign_variables(included_content)
        merge_variables_from_include(variables)
        included_content = extract_components(included_content)
        included_content = extract_hashmaps(included_content)
        return included_content
    except requests.RequestException as e:
        print(f"Error fetching native component {filename}: {e}")
        return ''

def extract_includes(mml_content):
    """
    Process !include and !include native statements to make components, variables, and hashmaps accessible.
    """

    # First, handle native includes
    native_matches = re.findall(r'!include\s+native\s*\[\s*(.*?)\s*\]', mml_content)
    for match in native_matches:
        included_content = process_native_include(re.match(r'(.*)', match))
        mml_content = mml_content.replace(f'!include native [{match}]', included_content)

    # Then handle normal local/remote includes (without .package)
    include_matches = re.findall(r'!include\s*\[\s*(.*?)\s*\]', mml_content)
    for path in include_matches:
        try:
            if path.startswith(('http://', 'https://')):
                # Handle remote files
                response = requests.get(path)
                response.raise_for_status()
                included_content = response.text
            else:
                # Handle local files or folders
                if os.path.isdir(path):
                    included_content = ''
                    for root, _, files in os.walk(path):
                        for file in files:
                            if file.endswith('.mml'):
                                with open(os.path.join(root, file), 'r') as f:
                                    included_content += f.read() + '\n'
                else:
                    with open(path, 'r') as f:
                        included_content = f.read()
            
            # Recursively process includes in the included content
            variables.update(shared_variables)
            included_content = extract_includes(included_content)
            included_content = extract_variables(included_content)
            included_content = assign_variables(included_content)
            merge_variables_from_include(variables)
            included_content = extract_components(included_content)
            included_content = extract_hashmaps(included_content)

            # Remove the include statement
            mml_content = mml_content.replace(f'!include [{path}]', '')

        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except requests.RequestException as e:
            print(f"Error fetching {path}: {e}")

    return mml_content

def extract_variables(mml_content):
    """
    Extract typed variables (static/dynamic) and store in the variables dict.
    Supports static <type> name = value and dynamic name = value.
    """
    # Match static vars: static <type> name = value
    static_matches = re.findall(r'static\s+(str|i32|float|list|bool|nonetype|complex|vec2i|vec3i|vecf|uuid|bit|char|color)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', mml_content)
    for datatype, var_name, var_value in static_matches:
        var_value = substitute_variables(var_value.strip())
        evaluated_value = safe_eval(var_value, datatype)
        variables[var_name] = {"datatype": datatype, "vartype": "static", "value": evaluated_value}
    
    # Match dynamic vars: dynamic name = value
    dynamic_matches = re.findall(r'dynamic\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', mml_content)
    for var_name, var_value in dynamic_matches:
        var_value = substitute_variables(var_value.strip())
        evaluated_value = safe_eval(var_value, None)  # dynamic type
        variables[var_name] = {"datatype": type_name(evaluated_value), "vartype": "dynamic", "value": evaluated_value}

    # Remove declarations from MML content
    mml_content = re.sub(r'static\s+(str|i32|float|list|bool|nonetype|complex|vec2i|vec3i|vecf|uuid|bit|char|color)\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*[^\n]+', '', mml_content)
    mml_content = re.sub(r'dynamic\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*[^\n]+', '', mml_content)
    return mml_content

def assign_variables(mml_content):
    assignment_pattern = re.compile(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$', re.MULTILINE)

    def replace_assignment(match):
        var_name = match.group(1)
        var_value = match.group(2).strip()

        if var_name not in variables:
            return match.group(0)  # ignore undeclared vars

        var_info = variables[var_name]
        var_value = substitute_variables(var_value)

        if var_info["vartype"] == "static":
            evaluated_value = safe_eval(var_value, var_info["datatype"])
            # Only update if we got a valid value of the right type
            if evaluated_value is not None and type_name(evaluated_value) == var_info["datatype"]:
                var_info["value"] = evaluated_value
        else:  # dynamic
            evaluated_value = safe_eval(var_value, None)
            var_info["value"] = evaluated_value
            var_info["datatype"] = type_name(evaluated_value)

        return ''

    return assignment_pattern.sub(replace_assignment, mml_content)

def type_name(value):
    if isinstance(value, str) and len(value) == 1:
        return "char"
    elif isinstance(value, str):
        return "str"
    elif isinstance(value, int) and not isinstance(value, bool) and value in (0, 1):
        return "bit"
    elif isinstance(value, int) and not isinstance(value, bool):
        return "i32"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, list):
        return "list"
    elif isinstance(value, bool):
        return "bool"
    elif isinstance(value, complex):
        return "complex"
    elif isinstance(value, tuple):
        if len(value) == 2 and all(isinstance(v, int) for v in value):
            return "vec2i"
        if len(value) == 3 and all(isinstance(v, int) for v in value):
            return "vec3i"
        if len(value) == 2 and all(isinstance(v, float) for v in value):
            return "vecf"
    elif isinstance(value, uuid.UUID):
        return "uuid"
    elif value is None:
        return "nonetype"
    return "any"

def is_valid_color(value):
    try:
        # If this succeeds, it's a valid color
        Color(value)
        return True
    except:
        return False

def safe_eval(value, expected_type=None):
    value = value.strip()

    # Handle 'new uuidX' keyword
    if value.startswith("new "):
        if expected_type is None or expected_type == "uuid":
            parts = value.split()
            if len(parts) == 2 and parts[1].startswith("uuid"):
                version = parts[1][4:]
                try:
                    if version == "1":
                        return uuid.uuid1()
                    elif version == "3":
                        # For simplicity, use namespace DNS and some name
                        return uuid.uuid3(uuid.NAMESPACE_DNS, "example")
                    elif version == "4":
                        return uuid.uuid4()
                    elif version == "5":
                        return uuid.uuid5(uuid.NAMESPACE_DNS, "example")
                except:
                    return None
        return None

    # UUID literal: uuid['...']
    if value.startswith("uuid[") and value.endswith("]"):
        try:
            inside = value[5:-1].strip().strip("'").strip('"')
            return uuid.UUID(inside)
        except:
            return None

    # Vector parsing
    if value.startswith("v[") and value.endswith("]"):
        inside = value[2:-1].strip()
        parts = [p.strip() for p in inside.split(",")]

        try:
            if expected_type == "vec2i":
                if len(parts) == 2 and all(p.isdigit() for p in parts):
                    return (int(parts[0]), int(parts[1]))
            elif expected_type == "vec3i":
                if len(parts) == 3 and all(p.isdigit() for p in parts):
                    return (int(parts[0]), int(parts[1]), int(parts[2]))
            elif expected_type == "vecf":
                if len(parts) == 2 and all("." in p or p.replace(".", "", 1).isdigit() for p in parts):
                    return (float(parts[0]), float(parts[1]))
            else:
                # Dynamic vectors
                if all("." in p or p.replace(".", "", 1).isdigit() for p in parts):
                    return tuple(float(p) for p in parts)
                elif all(p.isdigit() for p in parts):
                    return tuple(int(p) for p in parts)
        except:
            return None
        return None
    
    # New color type
    if expected_type == "color":
        try:
            # For color["red"] style or color with kwargs
            if value.startswith("c[") and value.endswith("]"):
                inner = value[2:-1].strip()
                # Evaluate inner safely
                evaluated_inner = eval(inner)
                color_obj = Color(evaluated_inner)
                return color_obj
        except:
            return None

    # Normal eval
    try:
        result = eval(value)
    except:
        result = value.strip('"').strip("'")

    # Standard type checks
    if expected_type == "char" and isinstance(result, str) and len(result) == 1:
        return result 
    elif expected_type == "str" and isinstance(result, str):
        return result 
    elif expected_type == "bit" and isinstance(result, int) and not isinstance(result, bool) and result in (0, 1):
        return result
    elif expected_type == "i32" and isinstance(result, int) and not isinstance(result, bool):
        return result
    elif expected_type == "float" and isinstance(result, float):
        return result
    elif expected_type == "list" and isinstance(result, list):
        return result
    elif expected_type == "bool" and isinstance(result, bool):
        return result
    elif expected_type == "nonetype" and result is None:
        return result
    elif expected_type == "complex" and isinstance(result, complex):
        return result
    elif expected_type == "uuid" and isinstance(result, uuid.UUID):
        return result

    return None

def merge_variables_from_include(included_vars):
    """
    Merge variables from an included MML file into the shared_variables dict.
    Keeps the type/vartype/value structure.
    """
    for var_name, var_info in included_vars.items():
        # Only add if not already present in shared_variables
        if var_name not in shared_variables:
            shared_variables[var_name] = var_info
        else:
            # Optional: could override if you want included file to replace
            shared_variables[var_name] = var_info

def substitute_variables(mml_content):
	for var_name, var_info in variables.items():
		value = var_info["value"]
		# If it's a string, substitute raw value (no quotes)
		if isinstance(value, str):
			replacement = value
		else:
			replacement = str(value)
		mml_content = re.sub(f':{var_name}:', replacement, mml_content)
	return mml_content

def extract_hashmaps(mml_content):
    """
    Extract hashmaps from the MML content and store them in the global hashmaps dictionary.
    """
    map_matches = re.findall(r'map\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\{(.*?)\}', mml_content, re.DOTALL)
    for map_name, map_body in map_matches:
        hashmap = {}
        entries = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', map_body)
        for key, value in entries:
            value = substitute_variables(value.strip())
            try:
                evaluated_value = eval(value)
            except:
                evaluated_value = value.strip().strip('"').strip("'")
            hashmap[key] = evaluated_value
        hashmaps[map_name] = hashmap
    mml_content = re.sub(r'map\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\{.*?\}', '', mml_content, flags=re.DOTALL)
    return mml_content

def substitute_hashmaps(mml_content):
    """
    Substitute hashmaps in the MML content with their values.
    """
    for map_name, hashmap in hashmaps.items():
        for key, value in hashmap.items():
            mml_content = re.sub(f':{map_name}\.{key}:', str(value), mml_content)
    return mml_content

def extract_components(mml_content):
    """
    Extract components from the MML content and store them in the global components dictionary.
    """
    component_matches = re.findall(r'\$export\.([a-zA-Z_][a-zA-Z0-9_]*)\s*(.*?)\$/export', mml_content, re.DOTALL)
    for component_name, component_body in component_matches:
        components[component_name] = component_body.strip()
    mml_content = re.sub(r'\$export\.([a-zA-Z_][a-zA-Z0-9_]*)\s*.*?\$/export', '', mml_content, flags=re.DOTALL)
    return mml_content

def convert_component_to_html(component_body):
    """
    Convert a component's MML content to HTML.
    """
    component_body = re.sub(r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)', r'<\1\2>', component_body)
    component_body = re.sub(r'\.\&([a-zA-Z0-9]+)', r'</\1>', component_body)
    component_body = re.sub(r'cl\.\[([^\]]+)\]', r'class="\1"', component_body)
    component_body = re.sub(r'link\.\[([^\]]+)\]', r'href="\1"', component_body)
    component_body = re.sub(r'([a-zA-Z]+)\.\[([^\]]+)\]', r'\1="\2"', component_body)
    component_body = re.sub(r'([a-zA-Z]+)!"([^"]+)"', r'\1="\2"', component_body)
    component_body = re.sub(r'\{|\}', '', component_body)
    component_body = re.sub(r'<mml', r'<html', component_body)
    component_body = re.sub(r'<mml>', r'<html>', component_body)
    component_body = re.sub(r'</mml>', r'</html>', component_body)
    component_body = re.sub(r'<text', r'<p', component_body)
    component_body = re.sub(r'<text>', r'<p>', component_body)
    component_body = re.sub(r'</text>', r'</p>', component_body)
    component_body = re.sub(r'<ct', r'<div', component_body)
    component_body = re.sub(r'<ct>', r'<div>', component_body)
    component_body = re.sub(r'</ct>', r'</div>', component_body)
    component_body = re.sub(r'<js', r'<script', component_body)
    component_body = re.sub(r'<js>', r'<script>', component_body)
    component_body = re.sub(r'</js>', r'</script>', component_body)
    component_body = re.sub(r'<btn', r'<button', component_body)
    component_body = re.sub(r'<btn>', r'<button>', component_body)
    component_body = re.sub(r'</btn>', r'</button>', component_body)
    component_body = re.sub(r'<line', r'<hr', component_body)
    component_body = re.sub(r'<line>', r'<hr>', component_body)
    component_body = re.sub(r'<inct', r'<span', component_body)
    component_body = re.sub(r'<inct>', r'<span>', component_body)
    component_body = re.sub(r'</inct>', r'</span>', component_body)
    component_body = re.sub(r'<in', r'<input', component_body)
    component_body = re.sub(r'<in>', r'<input>', component_body)
    component_body = re.sub(r'</in>', r'</input>', component_body)
    return component_body

def substitute_components(mml_content):
    """
    Substitute components in the MML content with their HTML representation.
    """
    for component_name, component_body in components.items():
        component_html = convert_component_to_html(component_body)
        mml_content = re.sub(rf'\(@{component_name}\)', component_html, mml_content)
    return mml_content

def convert_mml_to_html(mml_content):
    """
    Convert MML content to HTML.
    """
    variables.update(shared_variables)
    mml_content = extract_includes(mml_content)
    mml_content = extract_variables(mml_content)
    mml_content = assign_variables(mml_content)
    mml_content = extract_hashmaps(mml_content)
    mml_content = extract_components(mml_content)
    mml_content = re.sub(r'doc!.mml', r'<!DOCTYPE html>', mml_content)
    mml_content = re.sub(r'!//', r'<!--', mml_content)
    mml_content = re.sub(r'//!', r'-->', mml_content)
    mml_content = re.sub(r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)', r'<\1\2>', mml_content)
    mml_content = re.sub(r'\.\&([a-zA-Z0-9]+)', r'</\1>', mml_content)
    mml_content = re.sub(r'cl\.\[([^\]]+)\]', r'class="\1"', mml_content)
    mml_content = re.sub(r'link\.\[([^\]]+)\]', r'href="\1"', mml_content)
    mml_content = re.sub(r'([a-zA-Z]+)\.\[([^\]]+)\]', r'\1="\2"', mml_content)
    mml_content = re.sub(r'([a-zA-Z]+)!"([^"]+)"', r'\1="\2"', mml_content)
    mml_content = re.sub(r'\{|\}', '', mml_content)
    mml_content = re.sub(r'<mml', r'<html', mml_content)
    mml_content = re.sub(r'<mml>', r'<html>', mml_content)
    mml_content = re.sub(r'</mml>', r'</html>', mml_content)
    mml_content = re.sub(r'<text', r'<p', mml_content)
    mml_content = re.sub(r'<text>', r'<p>', mml_content)
    mml_content = re.sub(r'</text>', r'</p>', mml_content)
    mml_content = re.sub(r'<ct', r'<div', mml_content)
    mml_content = re.sub(r'<ct>', r'<div>', mml_content)
    mml_content = re.sub(r'</ct>', r'</div>', mml_content)
    mml_content = re.sub(r'<js', r'<script', mml_content)
    mml_content = re.sub(r'<js>', r'<script>', mml_content)
    mml_content = re.sub(r'</js>', r'</script>', mml_content)
    mml_content = re.sub(r'<btn', r'<button', mml_content)
    mml_content = re.sub(r'<btn>', r'<button>', mml_content)
    mml_content = re.sub(r'</btn>', r'</button>', mml_content)
    mml_content = re.sub(r'<line', r'<hr', mml_content)
    mml_content = re.sub(r'<line>', r'<hr>', mml_content)
    mml_content = re.sub(r'<inct', r'<span', mml_content)
    mml_content = re.sub(r'<inct>', r'<span>', mml_content)
    mml_content = re.sub(r'</inct>', r'</span>', mml_content)
    mml_content = re.sub(r'<in', r'<input', mml_content)
    mml_content = re.sub(r'<in>', r'<input>', mml_content)
    mml_content = re.sub(r'</in>', r'</input>', mml_content)
    mml_content = substitute_components(mml_content)
    mml_content = substitute_hashmaps(mml_content)
    mml_content = substitute_variables(mml_content)
    return mml_content

def compile_mml_to_html(input_file, output_file):
    """
    Compile an MML file to an HTML file.
    """
    with open(input_file, "r") as mml_file:
        mml_content = mml_file.read()
    html_content = convert_mml_to_html(mml_content)
    html_content = re.sub(r'\n\s*\n', r'\n', html_content)
    with open(output_file, "w") as html_file:
        html_file.write(html_content)

# Main execution
input_mml_file_name = input("Provide a valid .mml file (without the .mml suffix): ")
input_mml_file = input_mml_file_name + ".mml"
output_html_file = input_mml_file_name + ".html"
compile_mml_to_html(input_mml_file, output_html_file)