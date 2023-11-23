def calc_val(x, deg, cf):
    res = 0
    for i in range(deg, -1, -1):
        res += cf[deg - i] * (x ** deg)
    return res


def input_dat():
    v1 = int(input("Введите степень полинома: "))
    v2 = int(input("Введите значение x0: "))
    v3 = list(map(int, input("Введите через пробел значения коэффициентов: ").split()))
    return v1, v2, v3


def print_divider(s, ln=40):
    print(s * ln)


def main():
    n, x0, A = input_dat()
    print_divider('_')
    p = calc_val(x0, n, A)

    A_d = A[::]
    kn = n
    for i in range(len(A)):
        A_d[i] *= kn
        kn -= 1

    p1 = calc_val(x0, n - 1, A_d)
    print(f'Значение многочлена в точке x0: {p}')
    print(f'Значение производной многочлена в точке x0: {p1}')


if __name__ == "__main__":
    main()