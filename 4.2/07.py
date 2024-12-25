results = []


def enter_results(*res):
    for r in res:
        results.append(r)


def get_sum():
    amount = [0, 0]
    for i in range(len(results)):
        if i % 2 == 0:
            amount[0] += results[i]
        else:
            amount[1] += results[i]
    return tuple(amount)


def get_average():
    avg = list(get_sum())
    d = len(results) // 2
    avg[0], avg[1] = round(avg[0] / d, 2), round(avg[1] / d, 2)
    return tuple(avg)
        

def main():
    enter_results(1, 2, 3, 4, 5, 6)
    print(get_sum(), get_average())
    enter_results(1, 2)
    print(get_sum(), get_average())


if __name__ == "__main__":
    main()