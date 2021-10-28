from os import path

dirname = path.join(path.dirname(__file__), '..',
                       '..', 'dictionaries', 'input', 'input.xdxf')


def write_data_file(dict_data):
    input_file = open(dirname, 'w')
    input_file.write(dict_data)
