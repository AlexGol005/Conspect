for i in range(11):
    for j in range(11):
        a = str(i*j).rjust(3, " ")
        print(a, end=" ")
    print()