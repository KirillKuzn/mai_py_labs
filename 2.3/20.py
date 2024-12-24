def check_blockchain(blocks):
        h_pred = 0
        for i, bn in enumerate(blocks):
            hn = bn % 256
            rn = (bn // 256) % 256
            mn = bn // (256 ** 2)
            if hn >= 100 or hn != (37 * (mn + rn + h_pred)) % 256:
                return i  
            h_pred = hn
        return -1


def main():
    n = int(input())
    blocks = [int(input()) for i in range(n)]
    res = check_blockchain(blocks)
    print(res)



if __name__ == "__main__":
    main()