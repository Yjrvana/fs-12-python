def eratosthenes_sieve(n):
    a = [True] * (n + 1)
    res = []
    for k in range(2, n + 1):
        if a[k]:
            res.append(k)
            for i in range(k * k, n + 1, k):
                a[i] = False
    return res


def solve(x):
    primes = eratosthenes_sieve(x)
    for i in range(len(primes) - 1, -1, -1):
        if x % primes[i] == 0:
            return primes[i]
    return -1


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


def main():
    print(solve(21))


if __name__ == "__main__":
    main()
