import operator
import numpy as np
from funcs import get_training_data, calc_distance


def classify(user_input_arr, k_variable):
    training_data_arr = get_training_data()
    training_data_arr_good = training_data_arr[:, :4]  # get fist 4 columns - only user input
    training_data_last_column_arr = training_data_arr[:, -1]  # get only last column - type of flower
    # explanation - http://www.i-programmer.info/programming/python/3942-arrays-in-python.html

    flower_type_and_distance_dictionary = {}

    for idx, val in enumerate(training_data_arr_good):
        distance_rez = calc_distance(val, user_input_arr)  # calc distance
        flower_type = training_data_last_column_arr[idx]  # get type of flower
        flower_type_and_distance_dictionary[distance_rez] = flower_type  # Key - flower type; Value = distance

    sorted_flower_type_and_distance_dict = sorted(flower_type_and_distance_dictionary.items(),
                                                  key=operator.itemgetter(0))  # sort dict

    first_k_elements = sorted_flower_type_and_distance_dict[:k_variable]
    k_most_freq_labels = list()
    for element in first_k_elements:
        k_most_freq_labels.append(element[1])  # add labels to list

    counts = np.bincount(k_most_freq_labels) # finding the most "popular" flower
    final_result = np.argmax(counts)
    return final_result