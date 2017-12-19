import fuzzy_helpers

items = [
    "T-SHIRT",
    "CAP",
    'LONG SLEEVE'
]

experts = [
    [
        [1, .6, .4],
        [.5, 1, .6],
        [.4, .5, 1]
    ],
    [
        [1, .5, .5],
        [.5, 1, .1],
        [.4, .7, 1]
    ],
    [
        [1, .5, .4],
        [.2, 1, .1],
        [.1, .7, 1]
    ]
]

relation_matrix = fuzzy_helpers.fuzzy_convolution(experts, items)
non_dominate = fuzzy_helpers.non_dominate_alternatives(relation_matrix, items)
result = fuzzy_helpers.select_max_alternatives(non_dominate)

print("U*:", list(map(lambda i: items[i], result)))
