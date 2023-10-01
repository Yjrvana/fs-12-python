A = set(map(int, input().split()))
B = set(map(int, input().split()))
n_A = sum(map(lambda p: 2 ** p, A))
n_B = sum(map(lambda p: 2 ** p, B))
n_res = n_A & n_B
for i in range(0, 32):
    if n_res % 2 == 1:
        print(i, end=" ")
    n_res //= 2
