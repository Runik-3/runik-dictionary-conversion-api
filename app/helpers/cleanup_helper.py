import os
from shutil import rmtree

output_dir = os.path.join(os.path.dirname(__file__), '..',
                        '..', 'dictionaries', 'output')

# cleans up the output folder
def cleanup(response):
    rmtree(output_dir)
    os.mkdir(output_dir)
    return response
