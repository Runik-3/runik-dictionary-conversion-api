from os import system
from os import path
import subprocess


def convert_kobo_dictionary(dictionary_title, input_format):
    # apply file format text formatting
    if input_format == 'xdxf':
        input_format = 'Xdxf'

    input_path = path.join(path.dirname(__file__), '..',
                        '..', '..','dictionaries', 'input', 'input.xdxf')

    output_path = path.join(path.dirname(__file__), '..',
                       '..', '..','dictionaries', 'output', f'dicthtml-{dictionary_title}-en.kobo.zip')

    cmd_string = f'pyglossary -v1 {input_path} {output_path} --read-format={input_format} --write-format=Kobo'
    cmd_array = cmd_string.split()

    subprocess.run(cmd_array)

    return output_path

def convert_kindle_dictionary(dictionary_title, input_format):
    return False