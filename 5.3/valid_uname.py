class BadCharacterError(Exception):
    pass

class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    
    alphabet = (
        [ord('_')] 
        + list(range(ord('A'), ord('Z') + 1))
        + list(range(ord('a'), ord('z') + 1))
        + list(range(ord('0'), ord('9') + 1)))
    
    if not all(ord(s) in alphabet for s in username):
        raise BadCharacterError
    
    if ord(username[0]) in list(range(ord('0'), ord('9') + 1)):
        raise StartsWithDigitError
    
    return username


