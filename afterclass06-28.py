import random
array=""
for x in range(10):
    number= random.randint(1, 999)
    array = array +" "+ str(number)
a = 3
b = 11
for i in range (0,a):
    for j in range(0,b):
        if i == 0  or i == a-1 : 
            print("---", end='')
        else:
            print(array[j],"|", end='')
    print()