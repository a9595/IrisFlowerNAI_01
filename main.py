import operator
import numpy as np

from funcs import calc_distance
from funcs import get_training_data

# init vars
trainingDataArr = get_training_data()
trainingDataArrGood = trainingDataArr[:, :4]
trainingDataLastColumnArr = trainingDataArr[:, -1]
userInputArr = [1, 2, 3, 4]  # TODO: user input
distances_arr = []
dictionaryData = {}

# user input:
userInputArr[0] = int(input("Enter arg 1: "), 10)
userInputArr[1] = int(input("Enter arg 2: "), 10)
userInputArr[2] = int(input("Enter arg 3: "), 10)
userInputArr[3] = int(input("Enter arg 4: "), 10)

k_variable = int(input("Enter K: "), 10)

# let's play bro
distance_rez = 0
for idx, val in enumerate(trainingDataArrGood):
    distance_rez = calc_distance(val, userInputArr)  # calc distance
    flower_type = trainingDataLastColumnArr[idx]  # get type of flower
    # print("#", idx, " = ", distance_rez, " (", flower_type, ")")
    distances_arr.append(distance_rez)
    dictionaryData[distance_rez] = flower_type  # Key - flower type; Value = distance

sorted_dict = sorted(dictionaryData.items(), key=operator.itemgetter(0))  # sort dict

# print first K elements
for idx, val in enumerate(sorted_dict[:k_variable]):
    print("# ", idx, " = ", val)


# _--------------

first_K_elements = sorted_dict[:k_variable]
k_most_freq_labels = list()
for element in first_K_elements:
    print("Element - ", element[1])
    k_most_freq_labels.append(element[1])  # add labels to list

print(k_most_freq_labels)

counts = np.bincount(k_most_freq_labels)
print("Most frequent label= ", np.argmax(counts))



# find most frequent flower
# list_of_types = dict(sorted_dict.values())
#
# counts = np.bincount(list_of_types)
# print(np.argmax(counts))


# distances_arr.sort()
# print("SORTED arr  ", distances_arr)


