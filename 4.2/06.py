def order(*drinks):
    menu = {
        "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
        "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
        "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
        "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
    }
    drink = 'К сожалению, не можем предложить Вам напиток'
    for d in drinks:
        for ingr in menu[d].keys():
            if in_stock[ingr] < menu[d][ingr]:
                break
        else:
            for ingr in menu[d].keys():
                in_stock[ingr] -= menu[d][ingr]
            drink = d
            break
    return drink
            
        
def main():
    global in_stock
    in_stock = {"coffee": 1, "milk": 2, "cream": 3}
    print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
    print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))


if __name__ == "__main__":
    main()       
