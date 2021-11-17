def anonymous(f,a,b):
    return f(a,b)

print(anonymous(lambda a , b: "True" if a > b else "False",9,6 ))