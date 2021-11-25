from app.helpers.write_data_file_helper import write_data_file 
from app.helpers.converters.convert_dictionary_helper import convert_kobo_dictionary, convert_stardict_dictionary


def dictionary_handler(target_device, dictionary_title, input_format, request):
    target_device = target_device.lower()
    dict_data = request.get_data().decode('utf-8')
    output_path = ''

    # writes incoming dict to file to be converted 
    write_data_file(dict_data)

    # converts incoming dict from XDXF and returns to the correct format 
    if target_device == 'kobo': 
        output_path = convert_kobo_dictionary(dictionary_title, input_format)

    elif target_device == 'stardict': 
        output_path = convert_stardict_dictionary(dictionary_title, input_format)

    else:
        output_path = False



    return output_path