from classifier import classify


user_input = []
for i in range(0, 4):
    user_input.append(int(input("Enter arg: "), 10))

k_variable = int(input("Enter K: "), 10)

final_result = classify(user_input, k_variable)

print("final rez = ", final_result)