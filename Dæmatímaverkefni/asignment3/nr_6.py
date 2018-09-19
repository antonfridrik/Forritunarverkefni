AB = int(input("Input a two digit number: "))
C = 1
CAB = AB**2
while 1 <= C <= 9:
    if AB**2 == int(str(C) + str(AB)):
        print(CAB) 
    C += 1