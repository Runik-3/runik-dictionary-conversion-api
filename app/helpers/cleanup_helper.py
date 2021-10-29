from os import path
from shutil import rmtree

output_dir = path.join(path.dirname(__file__), '..',
                        '..', 'dictionaries', 'output')

# cleans up the output folder
def cleanup(response):
    rmtree(output_dir)
    return response
