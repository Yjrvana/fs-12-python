def solve(arr, k):
    sum_k = sum(arr[:k])
    max_sum_k = sum_k
    for i in range(k, len(arr)):
        sum_k += arr[k]
        sum_k -= arr[i - k]
        max_sum_k = max(max_sum_k, sum_k)
    return max_sum_k


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))


if __name__ == "__main__":
    main()