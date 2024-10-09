import re

# Dictionary to store variables and components
variables = {}
components = {}

def extract_variables(mml_content):
    # Extract variable declarations (supports int, float, string)
    var_matches = re.findall(r'var\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', mml_content)
    
    for var_name, var_value in var_matches:
        # Replace variables inside the value (like :var_name:)
        var_value = substitute_variables(var_value.strip())
        
        # Evaluate the expression using Python's eval
        try:
            # Handle numbers (integers or floats) and expressions
            evaluated_value = eval(var_value)
        except:
            # If eval fails (e.g. for strings), store as-is
            evaluated_value = var_value.strip().strip('"').strip("'")
        
        # Store the variable in the dictionary
        variables[var_name] = evaluated_value

    # Remove variable declarations from the original content
    mml_content = re.sub(r'var\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', '', mml_content)

    return mml_content

def substitute_variables(mml_content):
    # Replace instances of :var_name: with the corresponding variable value
    for var_name, var_value in variables.items():
        mml_content = re.sub(f':{var_name}:', str(var_value), mml_content)
    
    return mml_content

def extract_components(mml_content):
    # Extract components from MML content
    component_matches = re.findall(r'\$export\.([a-zA-Z_][a-zA-Z0-9_]*)\s*(.*?)\$/export', mml_content, re.DOTALL)
    
    for component_name, component_body in component_matches:
        components[component_name] = component_body.strip()

    # Remove component definitions from the original content
    mml_content = re.sub(r'\$export\.([a-zA-Z_][a-zA-Z0-9_]*)\s*.*?\$/export', '', mml_content, flags=re.DOTALL)

    return mml_content

def convert_component_to_html(component_body):
    # Convert component body to HTML
    component_body = re.sub(r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)', r'<\1\2>', component_body)  # Tag conversion
    component_body = re.sub(r'\.\&([a-zA-Z0-9]+)', r'</\1>', component_body)  # Closing tag conversion
    # Additional conversions as needed
    component_body = re.sub(r'cl\.\[([^\]]+)\]', r'class="\1"', component_body)  # Class conversion
    component_body = re.sub(r'link\.\[([^\]]+)\]', r'href="\1"', component_body)  # Link conversion
    component_body = re.sub(r'([a-zA-Z]+)\.\[([^\]]+)\]', r'\1="\2"', component_body)  # attr.[value] to attr="value"
    component_body = re.sub(r'([a-zA-Z]+)!"([^"]+)"', r'\1="\2"', component_body)  # attr!"value" to attr="value"
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
    return component_body

def substitute_components(mml_content):
    # Replace component usage with actual component content
    for component_name, component_body in components.items():
        component_html = convert_component_to_html(component_body)
        mml_content = re.sub(rf'\(@{component_name}\)', component_html, mml_content)
    return mml_content

def convert_mml_to_html(mml_content):
    # Step 1: Extract variables from MML content
    mml_content = extract_variables(mml_content)

    # Step 2: Extract components from MML content
    mml_content = extract_components(mml_content)
    
    # Step 3: Perform MML to HTML conversion
    # Standard MML to HTML conversions
    mml_content = re.sub(r'doc!.mml', r'<!DOCTYPE html>', mml_content)
    mml_content = re.sub(r'!//', r'<!--', mml_content)
    mml_content = re.sub(r'//!', r'-->', mml_content)

    # Convert tags like (&tag attr="value") and self-closing ones like (&img src="...")
    mml_content = re.sub(r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)', r'<\1\2>', mml_content)

    # Convert closing tags like .&tag to </tag>
    mml_content = re.sub(r'\.\&([a-zA-Z0-9]+)', r'</\1>', mml_content)

    # Handle custom attributes like cl.[value] and attr.[value]
    mml_content = re.sub(r'cl\.\[([^\]]+)\]', r'class="\1"', mml_content)
    mml_content = re.sub(r'link\.\[([^\]]+)\]', r'href="\1"', mml_content)
    mml_content = re.sub(r'([a-zA-Z]+)\.\[([^\]]+)\]', r'\1="\2"', mml_content)  # attr.[value] to attr="value"
    mml_content = re.sub(r'([a-zA-Z]+)!"([^"]+)"', r'\1="\2"', mml_content)

    # Remove leftover curly braces
    mml_content = re.sub(r'\{|\}', '', mml_content)

    # Special element conversions for mml, text, ct, etc.
    mml_content = re.sub(r'<mml', r'<html', mml_content)
    mml_content = re.sub(r'<mml>', r'<html>', mml_content)
    mml_content = re.sub(r'</mml>', r'</html>', mml_content)
    mml_content = re.sub(r'<text', r'<p', mml_content)
    mml_content = re.sub(r'<text>', r'<p>', mml_content)
    mml_content = re.sub(r'</text>', r'</p>', mml_content)
    mml_content = re.sub(r'<ct', r'<div', mml_content)
    mml_content = re.sub(r'<ct>', r'<div>', mml_content)
    mml_content = re.sub(r'</ct>', r'</div>', mml_content)

    # Step 4: Substitute variables and components in the content
    mml_content = substitute_components(mml_content)
    mml_content = substitute_variables(mml_content)

    return mml_content

def compile_mml_to_html(input_file, output_file):
    with open(input_file, "r") as mml_file:
        mml_content = mml_file.read()
    html_content = convert_mml_to_html(mml_content)
    html_content = re.sub(r'\n\s*\n', r'\n', html_content)  # Remove extra newlines
    with open(output_file, "w") as html_file:
        html_file.write(html_content)

# Example Usage
input_mml_file_name = input("Provide a valid .mml file (without the .mml suffix): ")
input_mml_file = input_mml_file_name + ".mml"
output_html_file = input_mml_file_name + ".html"
compile_mml_to_html(input_mml_file, output_html_file)
