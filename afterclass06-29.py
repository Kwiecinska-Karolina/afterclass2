array_1 = [8,3,1,2,5]
array_2 = [8,3,6,2,5,3,1,6,7,34,6]

if array_1 == array_2:
    print("yes")

for i in array_1:
    if i in array_2:
        print("yes")
    elif i not in array_2:
        print("no")
        
