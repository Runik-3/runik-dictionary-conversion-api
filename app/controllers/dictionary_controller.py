from app.helpers.write_data_file_helper import write_data_file 
from app.helpers.convert_dictionary_helper import convert_dictionary


def dictionary_handler(target_device, dictionary_title, input_format, request):
    dict_data = request.get_data().decode('utf-8')

    # writes incoming dict to file to be converted 
    write_data_file(dict_data)

    # converts incoming dict from XDXF and returns to the correct format 
    output_path = convert_dictionary(target_device, dictionary_title, input_format) 

    return output_path