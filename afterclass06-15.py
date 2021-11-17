array = ["pink", "blue","red","yellow","white","black","green","purple"]
colors=""
for i in array:
    colors = colors + " " +i
file = open("newfile.txt", "w")
file.write(colors)
file.close()