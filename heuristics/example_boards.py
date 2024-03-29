BOARDS = [
    # 0
    [
        [4, 0, 0, 4],
        [2, 0, 2, 0],
        [0, 64, 16, 0],
        [2, 0, 4, 0]
    ],
    # 1
    [[2, 0, 0, 2],
     [2, 0, 2, 0],
     [0, 64, 16, 0],
     [2, 0, 4, 0]],

    # 2
    [[4, 64, 64, 2],
     [0, 4, 4, 2],
     [0, 0, 0, 0],
     [0, 64, 0, 64]],

    # 3
    [[64, 2, 4, 64],
     [4, 4, 0, 2],
     [0, 0, 0, 0],
     [64, 0, 0, 64]],  # best for heu1

    # 4
    [
        [4, 0, 4, 8],
        [0, 0, 0, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 8]
    ],
    # 5
    [
        [4, 0, 2, 8],
        [0, 0, 0, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 4]
    ],
    # 6
    [
        [4, 0, 4, 64],
        [0, 0, 0, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 64]
    ],
    # 7  # 1 merge but big value
    [
        [0, 2, 4, 8],
        [2, 4, 2, 8],
        [0, 0, 0, 2],
        [0, 0, 0, 256]
    ],
    # 8  # 4 merge but low values
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [4, 0, 0, 16],
        [128, 16, 4, 128]
    ],
    # 9 # monotonicity good
    [
        [16, 8, 4, 2],
        [8, 4, 2, 0],
        [4, 2, 0, 0],
        [2, 0, 0, 0]
    ],
    # 10 # monotonicity bad
    [
        [2, 8, 4, 0],
        [2, 4, 16, 0],
        [4, 8, 2, 0],
        [2, 0, 0, 0]
    ],
    # 11
    [
        [0, 0, 0, 0],
        [0, 4, 16, 0],
        [0, 8, 2, 0],
        [0, 0, 0, 0]
    ],
    # 12
    [
        [2, 4, 2, 4],
        [0, 8, 32, 0],
        [0, 0, 0, 64],
        [0, 0, 0, 16]
    ],
    # 13
    [
        [4, 0, 0, 32],
        [16, 0, 4, 0],
        [64, 0, 32, 0],
        [16, 8, 4, 4]
    ],
    # 14
    [
        [4, 0, 0, 4],
        [2, 0, 0, 2],
        [0, 16, 32, 0],
        [32, 0, 64, 0]
    ],
    # 15
    [
        [0, 2, 2, 0],
        [0, 4, 0, 8],
        [8, 0, 0, 8],
        [2, 0, 16, 0]
    ],
    # 16
    [
        [8, 0, 4, 0],
        [0, 2, 2, 0],
        [32, 0, 0, 32],
        [16, 0, 8, 0]
    ],
    # 17
    [
        [8, 0, 4, 0],
        [0, 2, 0, 4],
        [16, 0, 0, 16],
        [4, 0, 2, 0]
    ],
    # 18
    [
        [16, 2, 0, 2],
        [8, 8, 2, 0],
        [4, 4, 0, 0],
        [2, 2, 0, 0]
    ],
    # 19
    [
        [2, 2, 0, 16],
        [2, 4, 16, 8],
        [64, 4, 0, 0],
        [0, 64, 0, 8]
    ],
]
