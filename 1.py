# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

list_number = [15, 16, 2, 3, 1, 7, 5, 4, 10]
new_list = [list_number[i] for i in range(len(list_number)) if list_number[i-1] < list_number[i]]
print("List: " + str(list_number))
print("New List: " + str(new_list))