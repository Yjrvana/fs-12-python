def solve(matrix):
    rows_maxes = [0 for _ in range(len(matrix))]
    cols_mines = [-1 for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rows_maxes[i] = max(rows_maxes[i], matrix[i][j])
            if cols_mines[j] == -1 or cols_mines[j] > matrix[i][j]:
                cols_mines[j] = matrix[i][j]
    for i in range(len(rows_maxes)):
        if rows_maxes[i] == cols_mines[i]:
            return rows_maxes[i]
    return None


def main():
    a = [list(map(int, input().split())) for _ in range(10)]
    print(solve(a))


main()
