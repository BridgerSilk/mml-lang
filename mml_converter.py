#!/usr/bin/env python3

import re
import os
import requests
from urllib.parse import urljoin

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

def extract_includes(mml_content):
    """
    Process !include and !include.package statements to make components, variables, and hashmaps accessible.
    """
    # Regular expression to match both !include and !include.package
    include_matches = re.findall(r'!include(?:\.package)?\s*\[\s*(.*?)\s*\]', mml_content)
    
    for path in include_matches:
        try:
            if path.startswith(('http://', 'https://')):
                # Handle remote files or folders
                if path.endswith('.mml'):
                    # Single remote file
                    response = requests.get(path)
                    response.raise_for_status()
                    included_content = response.text
                else:
                    # Remote folder (e.g., GitHub repo)
                    included_content = ''
                    if 'github.com' in path:
                        # Extract owner, repo, and path from the GitHub URL
                        parts = path.replace('https://github.com/', '').split('/')
                        owner = parts[0]
                        repo = parts[1]
                        
                        # Handle the path correctly (remove 'tree/main' if present)
                        if parts[2] == 'tree':
                            folder_path = '/'.join(parts[4:])  # Skip 'tree' and branch name (e.g., 'main')
                        else:
                            folder_path = '/'.join(parts[2:])
                        
                        # Construct the GitHub API URL
                        api_url = f'https://api.github.com/repos/{owner}/{repo}/contents/{folder_path}'
                        response = requests.get(api_url)
                        response.raise_for_status()
                        files = response.json()
                        
                        for file in files:
                            if file['name'].endswith('.mml'):
                                file_url = file['download_url']
                                file_response = requests.get(file_url)
                                file_response.raise_for_status()
                                included_content += file_response.text + '\n'
                                print(file_response.text + '\n')
                    else:
                        # Handle other remote folders (not implemented here)
                        raise NotImplementedError("Only GitHub repos are supported for remote folders.")
            else:
                # Handle local files or folders
                if os.path.isdir(path):
                    # Local folder
                    included_content = ''
                    for root, _, files in os.walk(path):
                        for file in files:
                            if file.endswith('.mml'):
                                with open(os.path.join(root, file), 'r') as included_file:
                                    included_content += included_file.read() + '\n'
                else:
                    # Single local file
                    with open(path, 'r') as included_file:
                        included_content = included_file.read()
            
            # Recursively process includes in the included content
            included_content = extract_includes(included_content)
            
            # Extract variables, components, and hashmaps from the included content
            included_content = extract_variables(included_content)
            included_content = extract_components(included_content)
            included_content = extract_hashmaps(included_content)
            
            # Remove the include statement from the main content
            mml_content = mml_content.replace(f'!include [{path}]', '')
            mml_content = mml_content.replace(f'!include.package [{path}]', '')
        
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except requests.RequestException as e:
            print(f"Error: Failed to fetch {path} - {e}")
        except NotImplementedError as e:
            print(f"Error: {e}")
    
    return mml_content

def extract_variables(mml_content):
    """
    Extract variables from the MML content and store them in the global variables dictionary.
    """
    var_matches = re.findall(r'var\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', mml_content)
    for var_name, var_value in var_matches:
        var_value = substitute_variables(var_value.strip())
        try:
            evaluated_value = eval(var_value)
        except:
            evaluated_value = var_value.strip().strip('"').strip("'")
        variables[var_name] = evaluated_value
    mml_content = re.sub(r'var\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^\n]+)', '', mml_content)
    return mml_content

def substitute_variables(mml_content):
    """
    Substitute variables in the MML content with their values.
    """
    for var_name, var_value in variables.items():
        mml_content = re.sub(f':{var_name}:', str(var_value), mml_content)
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
    mml_content = extract_includes(mml_content)
    mml_content = extract_variables(mml_content)
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