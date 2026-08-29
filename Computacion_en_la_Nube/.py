x = 0
M = 0
a = 0

while x <= 1600:
    if(x / 8 == 0):
        print(x, "es multiplo")
        M = M + x
        x += 1
    else:
        print(x, "No es multiplo") 
        a = a + x
        x += 1

    print(x, end = "\t")


print(M) 
