from project.dictionaries import (
    en_us,
    pt_br
)


# Define dictionaries
dictionaries: dict[dict] = {
    'default': en_us.dictionary,
    'en_us': en_us.dictionary,
    'pt_br': pt_br.dictionary,
}
