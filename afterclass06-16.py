array = [12, 6, 4, 9 , 3]
n = 0
def star(n):
    for x in array:
        n = x
        for i in range (1,2):
            for j in range(0,n):
                print((i) * "*" ,end="")
            print("\r")
        
star(n)