def make_linear(prlist):
    newlist = []
    for el in prlist:
        if isinstance(el, list):
            newlist += make_linear(el)
        else:
            newlist.append(el)
    return newlist
    
    
def main():
    print(make_linear([1, [2, [3, 4]], 5, 6]))


if __name__ == "__main__":
    main()