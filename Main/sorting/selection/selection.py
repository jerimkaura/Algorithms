def selection_sort(unsorted):
    sorted =[]
    while len(unsorted) !=0:
        x = min(unsorted)
        sorted.append(x)
        unsorted.remove(x)
    print(sorted)

if __name__ == "__main__":
    list = [987, 9,6, 89, 90,90,90,123, 91, 13, 12, 34, 22, 56, 70, 45, 33]
    print(list)
    selection_sort(list)
   


