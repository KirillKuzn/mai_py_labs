def merge(n, m):
    len_n, len_m = len(n), len(m)
    i, j = 0, 0
    result = [0] * (len_n + len_m)
    while (i + j) < (len_n + len_m):
        x = float('inf') if i >= len_n else n[i]
        y = float('inf') if j >= len_m else m[j]
        if x > y:
            result[i + j] = y
            j += 1
        else:
            result[i + j] = x
            i += 1

    return tuple(result)


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        before_mid = merge_sort(nums[:mid])
        after_mid = merge_sort(nums[mid:])
        return list(merge(before_mid, after_mid))
    return nums
    

def main():
    print(merge_sort([3, 2, 1]))


if __name__ == "__main__":
    main()