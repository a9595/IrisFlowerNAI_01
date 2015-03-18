def calc_distance(data_arr, user_arr):
    sum_of_arrays = 0
    for (data, user) in zip(data_arr, user_arr):
        sum_of_arrays += (data - user) ** 2
        # print("a: ", data, "; b: ", user)
    return sum_of_arrays ** (1 / 2)

    # print(trainingDataArr[:, :4])  # get all beside last
    # print(trainingDataArr[:, -1])  # get last column