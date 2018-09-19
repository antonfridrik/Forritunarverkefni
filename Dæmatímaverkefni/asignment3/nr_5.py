n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
i = 2
toggle = 0

while i < n:
    if n % i == 0:
        print ("!Prime")
    i += 1
else: 
    print("Prime")
