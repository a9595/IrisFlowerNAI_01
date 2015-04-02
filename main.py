import difflib

import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import interp1d
from classifier import classify
from foo.upload_to_ploty_server import upload_to_internet

from funcs import get_user_input, get_test_data_inputs, get_test_data_outputs, get_flower_name


def calc_similarity(k_var=5, ):
    # global user_input, k_variable, most_popular_arr, test_data_inputs_arr, test_data_outputs_arr, data, sm, similarity
    # input
    # k_variable = int(input("Enter K: ")) #TODO: user input
    # user_input = get_user_input() #TODO: user input

    # k_variable = 150

    most_popular_arr = []
    test_data_inputs_arr = get_test_data_inputs().tolist()  # import test data inputs
    test_data_outputs_arr = get_test_data_outputs().tolist()  # import test data results
    for data in test_data_inputs_arr:
        most_popular_arr.append(classify(data, k_var))
    print("result most popular are: ", most_popular_arr)
    print("size = ", len(most_popular_arr))
    print("training data output:    ", test_data_outputs_arr)
    print("output test data size = ", len(test_data_outputs_arr))
    sm = difflib.SequenceMatcher(None, most_popular_arr, test_data_outputs_arr)
    similarity = sm.ratio() * 100
    print("similarity = ", similarity, "%")
    return similarity


def show_graph(x_arr, y_arr, x_label, y_label):
    plt.plot(x_arr, y_arr)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # make it smoother
    f2 = interp1d(x_arr, y_arr, kind='cubic')
    x_new = np.linspace(min(x_arr), max(y_arr),
                        100)  # change last param for   'smoothness' strength
    plt.plot(x_arr, y_arr, 'o', x_new, f2(x_new), '--')
    plt.savefig('files/graph_result.pdf', bbox_inches='tight')  # save to PDF
    plt.savefig('files/graph_result.png', bbox_inches='tight')  # save to PNG
    plt.show()

# init
k_values_arr = []
similarity_values_arr = []

range_start = 1
range_stop = 200
range_step = 8
k_range_arr = list(range(range_start, range_stop, range_step))
for k in k_range_arr:
    similarity_values_arr.append(calc_similarity(k))  # a add similarity results

k_values_arr = k_range_arr

print("SIMILAR % arr = ", similarity_values_arr)
print("SIMILAR size = ", len(similarity_values_arr))
print("k arr = ", k_values_arr)
print("k arr size = ", len(k_values_arr))

show_graph(k_values_arr, similarity_values_arr, "K values", "accuracy of result(%)")

upload_to_internet()

# user input
print("\n\n\n\n User input:")
while True:
    user_input_arr = get_user_input()
    k_variable = (int(input("Enter K:"), 10))
    final_flower_result = classify(user_input_arr, k_variable)
    print("Result = ", get_flower_name(final_flower_result))
