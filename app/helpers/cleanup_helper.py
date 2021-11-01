import os
from shutil import rmtree

input_path = os.path.join(os.path.dirname(__file__), '..',
                        '..', 'dictionaries', 'input')

output_dir = os.path.join(os.path.dirname(__file__), '..',
                        '..', 'dictionaries', 'output')

# cleans up the output folder
def cleanup(response):
    rmtree(input_path)
    rmtree(output_dir)
    os.mkdir(input_path)
    os.mkdir(output_dir)
    open(os.path.join(input_path, 'input.xdxf'), 'w')
    open(os.path.join(output_dir, 'init'), 'w')

    return response
