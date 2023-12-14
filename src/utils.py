import itertools


def get_column_wise(rows):
    a = []
    result = []
    for i in range(len(rows)):
        a = []
        for j in range(len(rows[0])):
            a.append((rows[i][j][1], rows[i][j][0]))
            result.append(a)
    return result


def get_diagonal_main(rows):
    return [
        rows[i][j]
        for i, j in itertools.product(range(len(rows)), range(len(rows[0])))
        if i == j
    ]


def get_diagonal_second(rows):
    return [
        rows[i][j]
        for i, j in itertools.product(range(len(rows)), range(len(rows[0])))
        if (i + j) == len(rows) - 1
    ]
