import numpy as np
from funcs import calc_distance

# init vars
trainingDataArr = np.array([[5.1, 3.5, 1.4, 0.2, 0],
                            [4.9, 3.0, 1.4, 0.2, 0],
                            [4.7, 3.2, 1.3, 0.2, 0],
                            [4.6, 3.1, 1.5, 0.2, 0]])

trainingDataArrGood = [[5.1, 3.5, 1.4, 0.2],
                       [4.9, 3.0, 1.4, 0.2],
                       [4.7, 3.2, 1.3, 0.2],
                       [4.6, 3.1, 1.5, 0.2]]

userInputArr = [1, 2, 3, 4]  # TODO: user input
distances_arr = []


# let's play bro

print(trainingDataArr[:, -1])  # get last column

distance_rez = 0
for idx, val in enumerate(trainingDataArrGood):
    distance_rez = calc_distance(val, userInputArr)
    print("#", idx, " distance = ", distance_rez)
    distances_arr.append(distance_rez)

print("distance_arr =  ", distances_arr)

flower_arr = np.append(trainingDataArr[:, -1], distances_arr, 1)
# flower_arr.shape
print("flower_arr = ", flower_arr)


