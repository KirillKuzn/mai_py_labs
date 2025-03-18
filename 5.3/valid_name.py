class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    
    cyrillic = (
        [ord("Ё"), ord("ё")]
        + list(range(ord("А"), ord("Я") + 1))
        + list(range(ord("а"), ord("я") + 1))
    )

    if not all(ord(letter) in cyrillic for letter in name):
        raise CyrillicError
    
    if name != name.capitalize():
        raise CapitalError
    
    return name