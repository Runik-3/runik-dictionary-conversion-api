def write_data_to_file(dict_data, dict_title):
    input_file = open('../dictionaries/input.xdxf', 'x')
    input_file.write(dict_data)
    print(input_file.read())
