def find_max(n):
    prev, cur, k = 1, 1, 1
    while 1:
        if cur > n >= prev:
            return prev, k
        k += 1
        prev, cur = cur, prev + cur


num = int(input())
res = 0
while num > 0:
    a1, a2 = find_max(num)
    num -= a1
    res += (2 ** (a2 - 2))
print(bin(res)[2:])