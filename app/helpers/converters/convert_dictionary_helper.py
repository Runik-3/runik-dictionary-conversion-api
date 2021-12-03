from os import system
from os import path
from shutil import make_archive

from pyglossary.glossary import Glossary

input_path = path.join(path.dirname(__file__), '..',
                        '..', '..','dictionaries', 'input', 'input.xdxf')

def convert_kobo_dictionary(dictionary_title, input_format):
    # apply file format text formatting
    if input_format == 'xdxf':
        input_format = 'Xdxf'
   
    output_path = path.join(path.dirname(__file__), '..',
                       '..', '..','dictionaries', 'output', f'dicthtml-{dictionary_title}-en.kobo.zip')

    glos = Glossary(
        info={"title": dictionary_title},
    )
    output_path = glos.convert(
        input_path,
        inputFormat=input_format,
        outputFilename=output_path,
        outputFormat="Kobo",
    )

    return output_path
