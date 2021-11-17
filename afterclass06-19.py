array = [2,3,2,5,8,1,9,8]
array.sort()
max=array[0]
for x in array:
    if x> max:
        max= x
for i in array:
    for j in array:
        if array[j-1] == array[j]:
            print("",end="")
        
        else:
            print(j)
    break
print(max)
   