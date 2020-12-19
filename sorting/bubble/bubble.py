# bubble_sort function
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp


list = [9, 6, 89, 123, 91, 13, 12, 34, 22, 56, 70, 45, 33]

# print the unsorted list
for i in range(len(list)):
    print(list[i], end=" ")
print("\n")

bubble_sort(list)

# print the soeted list
for i in range(len(list)):
    print(list[i], end=" ")
