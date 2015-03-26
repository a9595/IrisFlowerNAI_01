import operator
import numpy as np
from funcs import get_training_data, calc_distance


def classify(user_input_arr, k_variable):
    # global trainingDataArr, trainingDataArrGood, trainingDataLastColumnArr, userInputArr, distances_arr, dictionaryData, k_variable, distance_rez, idx, val, flower_type, sorted_dict, first_K_elements, k_most_freq_labels, element, counts
    training_data_arr = get_training_data()
    training_data_arr_good = training_data_arr[:, :4]
    training_data_last_column_arr = training_data_arr[:, -1]

    distances_arr = []
    dictionary_data = {}


    # let's play bro
    for idx, val in enumerate(training_data_arr_good):
        distance_rez = calc_distance(val, user_input_arr)  # calc distance
        flower_type = training_data_last_column_arr[idx]  # get type of flower
        # print("#", idx, " = ", distance_rez, " (", flower_type, ")")
        distances_arr.append(distance_rez)
        dictionary_data[distance_rez] = flower_type  # Key - flower type; Value = distance
    sorted_dict = sorted(dictionary_data.items(), key=operator.itemgetter(0))  # sort dict
    # print first K elements
    for idx, val in enumerate(sorted_dict[:k_variable]):
        print("# ", idx, " = ", val)

    first_k_elements = sorted_dict[:k_variable]
    k_most_freq_labels = list()
    for element in first_k_elements:
        print("Element - ", element[1])
        k_most_freq_labels.append(element[1])  # add labels to list
    print(k_most_freq_labels)
    counts = np.bincount(k_most_freq_labels)
    final_result = np.argmax(counts)
    # print("Most frequent label= ", final_result)
    return final_result