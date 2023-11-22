def bidirectional_bubble_sort(arr):
    left = 0
    right = len(arr)
    while left <= right:
        for i in range(left, right - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right - 1, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr


def main():
    arr_0 = [1, 6, 3, 5, 7, 8, 9, 10, 100, 3, -5, 1]
    print(bidirectional_bubble_sort(arr_0))


if __name__ == "__main__":
    main()
