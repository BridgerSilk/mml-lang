#!/usr/bin/env python3

# NOTE: this is obviously NOT an actual compiler, it is just for prototyping purposes to build a proper syntax before actually building the compiler!

import re

variables = {}
components = {}
hashmaps = {}

# todo - impl this syntax map sys
general_syntax_map = {
    r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)': r'<\1\2>', # () -> <>
    r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]+\]|\!"[^"]*"))*)\)': r'<\1\2>', # 
}

def extract_includes(mml_content):
    include_matches = re.findall(r'!include\s*\[\s*(.*?)\s*\]', mml_content)
    for file_name in include_matches:
        try:
            with open(file_name, 'r') as included_file:
                included_content = included_file.read()
            included_content = extract_includes(included_content)
            included_content = extract_variables(included_content)
            included_content = extract_components(included_content)
            included_content = extract_hashmaps(included_content)
            mml_content = mml_content.replace(f'!include [{file_name}]', included_content)
        except FileNotFoundError:
            print(f"Error: File {file_name} not found.")
    return mml_content

def extract_variables(mml_content):
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
    for var_name, var_value in variables.items():
        mml_content = re.sub(f':{var_name}:', str(var_value), mml_content)
    return mml_content

def extract_hashmaps(mml_content):
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
    for map_name, hashmap in hashmaps.items():
        for key, value in hashmap.items():
            mml_content = re.sub(f':{map_name}\.{key}:', str(value), mml_content)
    return mml_content

def extract_components(mml_content):
    component_matches = re.findall(r'\$export\.([a-zA-Z_][a-zA-Z0-9_]*)\s*(.*?)\$/export', mml_content, re.DOTALL)
    for component_name, component_body in component_matches:
        components[component_name] = component_body.strip()
    mml_content = re.sub(r'\$export\.([a-zA-Z_][a-zA-Z0-9_]*)\s*.*?\$/export', '', mml_content, flags=re.DOTALL)
    return mml_content

def convert_component_to_html(component_body):
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
    component_body = re.sub(r'<ctin', r'<span', component_body)
    component_body = re.sub(r'<ctin>', r'<span>', component_body)
    component_body = re.sub(r'</ctin>', r'</span>', component_body)
    return component_body

def substitute_components(mml_content):
    for component_name, component_body in components.items():
        component_html = convert_component_to_html(component_body)
        mml_content = re.sub(rf'\(@{component_name}\)', component_html, mml_content)
    return mml_content

def convert_mml_to_html(mml_content):
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
    mml_content = re.sub(r'<ctin', r'<span', mml_content)
    mml_content = re.sub(r'<ctin>', r'<span>', mml_content)
    mml_content = re.sub(r'</ctin>', r'</span>', mml_content)
    # hr doesnt have an end tag
    mml_content = substitute_components(mml_content)
    mml_content = substitute_hashmaps(mml_content)
    mml_content = substitute_variables(mml_content)
    return mml_content

def compile_mml_to_html(input_file, output_file):
    with open(input_file, "r") as mml_file:
        mml_content = mml_file.read()
    html_content = convert_mml_to_html(mml_content)
    html_content = re.sub(r'\n\s*\n', r'\n', html_content)
    with open(output_file, "w") as html_file:
        html_file.write(html_content)

input_mml_file_name = input("Provide a valid .mml file (without the .mml suffix): ")
input_mml_file = input_mml_file_name + ".mml"
output_html_file = input_mml_file_name + ".html"
compile_mml_to_html(input_mml_file, output_html_file)
