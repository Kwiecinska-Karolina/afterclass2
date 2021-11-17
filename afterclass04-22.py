def even(f,number):
    return f(number)

print(even(lambda number : "True" if number%2 == 0 else "False",2))
