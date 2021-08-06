from doctest import testmod


def get_name_abbreviation(name: str) -> str:
    """
    Generate name abbreviation with the first letters of the name and return
    it.

    Tests:
    >>> get_name_abbreviation('John Due')
    'JD'
    >>> get_name_abbreviation('John')
    'JO'
    >>> get_name_abbreviation('J')
    'JJ'
    >>> get_name_abbreviation('')
    '  '
    >>> get_name_abbreviation(None) == None
    True
    """
    if name is None:
        return None
    abbreviation = ''
    name_parts = name.split(' ')
    if len(name) == 0:
        abbreviation = '  '
    elif len(name) == 1:
        abbreviation = name[0] + name[0]
    elif len(name_parts) >= 2:
        abbreviation = name_parts[0][0] + name_parts[1][0]
    else:
        abbreviation = name_parts[0][0] + name_parts[0][1]
    return abbreviation.upper()


if __name__ == '__main__':
    testmod()
