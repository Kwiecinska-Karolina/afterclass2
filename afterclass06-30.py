def rand_elem(array):
    import random
    element= random.randint(array[0],array[len(array)-1])
    return element
array=[3,8,2,6,42,4,74,25,896,35,8,5,2,7]
print(rand_elem(array))
print(rand_elem(array))
print(rand_elem(array))