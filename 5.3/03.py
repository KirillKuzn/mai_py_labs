class Error:
    def __str__(self):
        raise Exception
    
    def __repr__(self):
        raise Exception
    

try:
    args = Error()
    # func(args)
except Exception:
    print('Ура! Ошибка!')