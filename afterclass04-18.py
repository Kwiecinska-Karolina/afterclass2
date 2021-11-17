def suma(liczba):

    liczba = list(liczba)
    sum = 0
    for i in liczba:
        sum = sum + int(i)
    return sum
    
print(suma("7182"))

