import re

def convert_mml_to_html(mml_content):

    # Standard MML to HTML conversions
    mml_content = re.sub(r'doc!.mml', r'<!DOCTYPE html>', mml_content)
    mml_content = re.sub(r'!//', r'<!--', mml_content)
    mml_content = re.sub(r'//!', r'-->', mml_content)

    # Convert empty square brackets to ""
    mml_content = re.sub(r'\.\[\]', r'=""', mml_content)

    # Convert tags like (&tag attr="value") and self-closing ones like (&img src="...")
    mml_content = re.sub(r'\(&([a-zA-Z0-9]+)((\s+[a-zA-Z]+(\.\[[^\]]*\]|\!"[^"]*"))*)\)', r'<\1\2>', mml_content)

    # Convert closing tags like .&tag to </tag>
    mml_content = re.sub(r'\.\&([a-zA-Z0-9]+)', r'</\1>', mml_content)

    # Handle attributes like attr.[value] and attr!"value"
    mml_content = re.sub(r'([a-zA-Z]+)\.\[([^\]]*)\]', r'\1="\2"', mml_content)  # Empty brackets handled here
    mml_content = re.sub(r'([a-zA-Z]+)!"([^"]+)"', r'\1="\2"', mml_content)

    # Special element conversions for mml, text, ct, etc.
    mml_content = re.sub(r'\(&mml', r'<html', mml_content)
    mml_content = re.sub(r'\.\&mml', r'</html>', mml_content)
    mml_content = re.sub(r'\(&text', r'<p', mml_content)
    mml_content = re.sub(r'\.\&text', r'</p>', mml_content)
    mml_content = re.sub(r'\(&ct', r'<div', mml_content)
    mml_content = re.sub(r'\.\&ct', r'</div>', mml_content)

    # Remove leftover curly braces
    mml_content = re.sub(r'[\{\}]', '', mml_content)

    # Remove extra closing brackets that remain
    mml_content = re.sub(r'[\)]', r'>', mml_content)

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