def binary_search(arr, k, order):
    low = 0
    high = len(arr) - 1
    r = 1 if order > 0 else -1
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] * r < k * r:
            low = mid + 1
        if arr[mid] * r > k * r:
            high = mid - 1
    return -1


def main():
    arr_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(binary_search(arr_0, 3, 1))
    print(binary_search(arr_1, 3, -1))


if __name__ == "__main__":
    main()