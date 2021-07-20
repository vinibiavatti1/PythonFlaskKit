from project.dictionaries.en_us import dictionary as en_us
from project.dictionaries.pt_br import dictionary as pt_br


# Dictionaries map
dictionaries = {
    'en_us': en_us,
    'pt_br': pt_br,
}


# Get dictionary
def get_dictionary(lang):
    """
    Get the dictionary by the specified lang
    Default is: en_us
    """
    dictionary = dictionaries.get(lang, None)
    if dictionary is None:
        dictionary = en_us
    return dictionary
