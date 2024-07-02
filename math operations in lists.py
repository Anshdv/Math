list_1 = [1, 2, 3]
list_2 = [2, 4, 6]

addition_list = []
subtraction_list = []
multiplication_list = []
division_list = []

list_elem = 0

while list_elem <= (len(list_1) - 1):
    addition_list.append((list_1[list_elem] + list_2[list_elem]))
    subtraction_list.append((list_1[list_elem] - list_2[list_elem]))
    multiplication_list.append((list_1[list_elem] * list_2[list_elem]))
    division_list.append((list_1[list_elem] / list_2[list_elem]))
    list_elem += 1

print(addition_list)
print(subtraction_list)
print(multiplication_list)
print(division_list)
