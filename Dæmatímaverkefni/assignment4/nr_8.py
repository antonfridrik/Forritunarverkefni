stars = int(input("Max number of stars: ")) # Do not change this line

for i in range(0,stars):
        for j in range(0,i+1):
                print("*", end="")
        print("")
for i in range(0,stars):
        for j in range(stars-1,i,-1):
                print("*", end="")
        print("")