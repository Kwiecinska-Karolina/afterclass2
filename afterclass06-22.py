array = [5,1,9,6,1]
max=array[0]
min=array[0]
for i in array:
    if i > max:
        max = i
    if i < min:
        min = i
        
        
difference = max - min
print(difference)