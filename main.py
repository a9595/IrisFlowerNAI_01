from array import array
import difflib
import matplotlib.pyplot as plt
import numpy as np
from classifier import classify
from funcs import get_user_input, get_test_data_inputs, get_test_data_outputs
from scipy.interpolate import interp1d


def calc_similarity(k_variable=5):
    # global user_input, k_variable, most_popular_arr, test_data_inputs_arr, test_data_outputs_arr, data, sm, similarity
    # input
    # k_variable = int(input("Enter K: ")) #TODO: user input
    # user_input = get_user_input() #TODO: user input
    user_input = [1, 2, 3, 4]

    # k_variable = 150

    most_popular_arr = []
    test_data_inputs_arr = get_test_data_inputs().tolist()  # import test data inputs
    test_data_outputs_arr = get_test_data_outputs().tolist()  # import test data results
    for data in test_data_inputs_arr:
        most_popular_arr.append(classify(data, k_variable))
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
    xnew = np.linspace(min(x_arr), max(y_arr),
                       100)  # change last param for   'smoothness' strength
    plt.plot(x_arr, y_arr, 'o', xnew, f2(xnew), '--')

    plt.show()

# init
k_values_arr = []
similarity_values_arr = []

r = list(range(1, 200, 8))
for k in r:
    similarity_values_arr.append(calc_similarity(k))  # a add similarity results

k_values_arr = r

print("SIMILAR % arr = ", similarity_values_arr)
print("SIMILAR size = ", len(similarity_values_arr))
print("k arr = ", k_values_arr)
print("k arr size = ", len(k_values_arr))

show_graph(k_values_arr, similarity_values_arr, "K values", "accuracy of result(%)")
# TODO: graf  = x(K) y(Similarity)