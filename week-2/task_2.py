def eratosthenes_sieve(n):
    a = [True] * (n + 1)
    res = []
    for k in range(2, n + 1):
        if a[k]:
            res.append(k)
            for i in range(k * k, n + 1, k):
                a[i] = False
    return res


def cmp_binary_search(arr, elem):
    if elem <= arr[0]:
        return 0
    if elem >= arr[-1]:
        return len(arr) - 1

    low = 0
    high = len(arr) - 1
    while high >= 0 and low < len(arr) - 1:
        mid = (low + high) // 2
        if (mid == len(arr) - 1) or (arr[mid] <= elem < arr[mid + 1]):
            return mid
        elif arr[mid] > elem:
            high = mid - 1
        elif arr[mid] < elem:
            low = mid + 1
    return -1


# non-optimal (zachem???...)
def solve(x):
    primes = eratosthenes_sieve(x)
    max_div = int(x ** 0.5) + 1
    return cmp_binary_search(primes, max_div)


# optimal(!)
# _______________________________
def solve_1(x):
    res, k = 0, 2
    while k * k <= x:
        if x % k == 0:
            res = x
            x //= k
        else:
            k += 1
    if x > 1:
        res = x
    return res
# ________________________________

def main():
    pass


if __name__ == "__main__":
    main()
