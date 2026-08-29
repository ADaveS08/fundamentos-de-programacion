
for i in range(10):
    for i in range(1,11,):
        if i == 4:
            print("@", end= " " )
        if i == 8 and i == 9:
            print("m", end= "m")
        if i != 4 and not (i == 8 and i == 9 ):
            print(i, end= " ")
    print()