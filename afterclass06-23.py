def median(array):

    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    if len(array)%2 == 0:
        a=len(array)//2
        b = array[a - 1]
        y = array[a]
        med = (b + y)/2
        print(med)
    elif len(array)%2 != 0:
        x = len(array)//2
        print(array[x])
    
array = [1,0,9,4,6]    
median(array)
array = [6,8,3,1,0,5,7]
median(array)