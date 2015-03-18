# import numpy as np
from funcs import calc_distance


trainingDataArr = [[5.1, 3.5, 1.4, 0.2, 0],
                   [4.9, 3.0, 1.4, 0.2, 0],
                   [4.7, 3.2, 1.3, 0.2, 0],
                   [4.6, 3.1, 1.5, 0.2, 0]]

trainingDataArrGood = [[5.1, 3.5, 1.4, 0.2],
                       [4.9, 3.0, 1.4, 0.2],
                       [4.7, 3.2, 1.3, 0.2],
                       [4.6, 3.1, 1.5, 0.2]]

userInputArr = [1, 2, 3, 4]  # T ODO: user input

distances_arr = []

for idx, val in enumerate(trainingDataArrGood):
    print("#", idx, " distance = ", calc_distance(val, userInputArr))