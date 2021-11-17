array = [2,1,5,2,87,6,4,3,9,5,52,7]
even = ""
odd=""
for i in array:
    if  i%2 == 0:
        even = even + " " +str(i)
    else:
        odd = odd +" " +str(i)
      
array = [even, odd]
print(array)
