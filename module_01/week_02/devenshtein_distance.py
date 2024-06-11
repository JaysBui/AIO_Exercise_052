# Bài 4:
import numpy as np


def devenshtein_distance(sc_wrds, targ_wrds):
    arr_nbr = np.zeros((len(sc_wrds) + 1, len(targ_wrds) + 1), dtype=int)

    for i in range(1, len(sc_wrds) + 1):
        arr_nbr[i][0] = i
    for j in range(1, len(targ_wrds) + 1):
        arr_nbr[0][j] = j

    del_cost = 1
    ins_cost = 1

    for i in range(1, len(sc_wrds) + 1):
        for j in range(1, len(targ_wrds) + 1):
            if sc_wrds[i - 1] == targ_wrds[j - 1]:
                sub_cost = 0
            else:
                sub_cost = 1
            del_expression = arr_nbr[i - 1][j] + del_cost
            ins_expression = arr_nbr[i][j - 1] + ins_cost
            sub_expression = arr_nbr[i - 1][j - 1] + sub_cost
            arr_nbr[i][j] = min(del_expression, ins_expression, sub_expression)
    devenshtein_distance = arr_nbr[-1][-1]
    print(devenshtein_distance)
    return devenshtein_distance


if __name__ == "__main__":
    devenshtein_distance("hola", "hello")
