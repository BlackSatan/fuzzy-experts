import numpy as np


def fuzzy_convolution(experts_matrix, items):
    return list(map(
        lambda row: list(map(
            lambda item: expert_matrix_min(experts_matrix, row, item),
            range(0, len(items))
        )),
        range(0, len(items))
    ))


def expert_matrix_min(experts_matrix, row, item):
    return min(map(lambda expert_matrix: expert_matrix[row][item], experts_matrix))


def strong_max(relation_matrix, row, item):
    first = relation_matrix[row][item]
    second = relation_matrix[item][row]
    if first <= second:
        return 0
    else:
        return first - second


def fuzzy_alternative(relation_matrix, items):
    return list(map(
        lambda item: 1 - max(map(
            lambda index: strong_max(relation_matrix, index, item),
            range(0, len(items))
        )),
        range(0, len(items))
    ))


def non_dominate_alternatives(relation_matrix, items):
    return list(map(
        lambda item: 1 - max(map(
            lambda index: strong_max(relation_matrix, index, item),
            range(0, len(items))
        )),
        range(0, len(items))
    ))


def select_max_alternatives(non_dominate_alternatives_list):
    max_val = max(non_dominate_alternatives_list)
    result = []
    for index, item in enumerate(non_dominate_alternatives_list):
        if item == max_val:
            result.append(index)
    return result
