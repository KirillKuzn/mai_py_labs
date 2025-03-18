from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


a = ([chr(n) for n in range(ord('0'), ord('9') + 1)]
     + [chr(c) for c in range(ord('A'), ord('Z') + 1)]
     + [chr(s) for s in range(ord('a'), ord('z') + 1)])


def password_validation(password, min_length=8, possible_chars=a, at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    
    if len(password) < min_length:
        raise MinLengthError
    
    if not all(s in possible_chars for s in password):
        raise PossibleCharError
    
    if not any(at_least_one(s) for s in password):
        raise NeedCharError
    
    return sha256(password.encode("UTF-8")).hexdigest()


# print(password_validation("Hello12345"))
# print(password_validation(
#     "uNrie_777",
#     min_length=6,
#     at_least_one=lambda char: char in "!@#$%^&*()_"
# ))
