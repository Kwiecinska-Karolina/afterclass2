def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
                
array = [19, 8, 4, 2, 7, 9, 4, 2, 6, 9, 6, 3, 65, 8, 4, 3, 5, 75, 52, 3, 6 , 4, 533 , 837, 3 , 13, 6, 2, 18, 8]
bubble_sort(array)
print(array)
