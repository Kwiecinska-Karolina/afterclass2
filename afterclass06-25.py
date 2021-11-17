def minmax(array):
 
    min = array[0] 
    max = array[0]

    for i in array:
        if i > max:
            max = i
        elif i < min:
            min = i
        
    array= [min, max]
    return array
array = [4,2,8,4,7,9,5]
print(minmax(array))

        