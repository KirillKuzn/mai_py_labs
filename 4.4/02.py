nums = []


def add_number(n):
    nums.append(n)


def get_prod():
    exp = ''
    prod = 1
    for i in range(0, len(nums)):
        if i == len(nums) - 1:
            exp += f'{nums[i]} ='
            prod *= nums[i]
        else:
            exp += f'{nums[i]} * '
            prod *= nums[i]
    exp += f' {prod}'
    return exp
            

def main():
    """Глобальное произведение"""

    add_number(1)
    add_number(2)
    add_number(3)
    print(get_prod())

    nums.clear()

    add_number(7)
    add_number(2)
    print(get_prod())
    add_number(5)
    print(get_prod())

if __name__ == "__main__":
    main()