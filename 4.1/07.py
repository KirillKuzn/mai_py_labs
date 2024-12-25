def can_eat(pos_a, pos_b):
    if abs(pos_a[0] - pos_b[0]) == 2 and abs(pos_a[1] - pos_b[1]) == 1:
        return True
    elif abs(pos_a[0] - pos_b[0]) == 1 and abs(pos_a[1] - pos_b[1]) == 2:
        return True
    else:
        return False
        

def main():
    print(can_eat((2, 1), (4, 2)))
    print(can_eat((5, 5), (6, 6)))


if __name__ == "__main__":
    main()