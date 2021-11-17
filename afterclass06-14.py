array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max = len(array[0])
for name in array:
    name = len(name)
    if name> max:
        max = name
for i in array:
    if len(i) == max:
        print(i)