import difflib
from classifier import classify
from funcs import get_user_input, get_test_data_inputs, get_test_data_outputs

# input
# k_variable = int(input("Enter K: ")) #TODO: user input
# user_input = get_user_input() #TODO: user input
user_input = [1, 2, 3, 4]
k_variable = 150

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
# good_results * 100 / size