for row in range(0,7):
    for column in range(6):
        if column==0 or (row==0 and row==4):
            print("*", end="")
    print()
