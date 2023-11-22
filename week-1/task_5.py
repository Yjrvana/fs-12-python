import math


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def factorial_zeros(n):
    r = 1
    res = 0
    while n // (5 ** r) > 0:
        res += n // (5 ** r)
        r += 1
    return res


def main():
    print(factorial(10))
    print(factorial_zeros(10))


if __name__ == "__main__":
    main()