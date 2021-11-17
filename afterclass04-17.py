def letters(zdanie, litera):
    ile=0 
    for i in zdanie:
        if i == litera:
            ile = ile + 1
    return ile
       
print(letters("You never get a second chance to make a first impression","e"))