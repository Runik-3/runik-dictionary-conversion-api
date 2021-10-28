from os import system
from os import path


def convert_dictionary(target_device, dictionary_title):
    input_path = path.join(path.dirname(__file__), '..',
                        '..', 'dictionaries', 'input', 'input.xdxf')
    output_path = dirname = path.join(path.dirname(__file__), '..',
                       '..', 'dictionaries', 'output', f'dicthtml-{dictionary_title}-en.kobo.zip')

    cmd = f''
    results = system(cmd)
    print(output_path)