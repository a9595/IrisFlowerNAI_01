import operator
from funcs import calc_distance
from funcs import get_training_data
# init vars
trainingDataArr = get_training_data()

trainingDataArrGood = trainingDataArr[:, :4]
trainingDataLastColumnArr = trainingDataArr[:, -1]
userInputArr = [1, 2, 3, 4]  # TODO: user input
distances_arr = []

dictionaryData = {}

# let's play bro
distance_rez = 0
for idx, val in enumerate(trainingDataArrGood):
    distance_rez = calc_distance(val, userInputArr)  # calc distance
    flower_type = trainingDataLastColumnArr[idx]  # get type of flower
    # print("#", idx, " = ", distance_rez, " (", flower_type, ")")
    distances_arr.append(distance_rez)
    dictionaryData[distance_rez] = flower_type  # Key - flower type; Value = distance

print(dictionaryData)

sorted_dict = sorted(dictionaryData.items(), key=operator.itemgetter(0))

print(sorted_dict)

# distances_arr.sort()
# print("SORTED arr  ", distances_arr)


