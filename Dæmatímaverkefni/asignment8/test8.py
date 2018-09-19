start_position = 1.1
position = start_position
direction = ""

while position <= 2.2:
    if position == 1.1:
        print("You can travel: (N)orth.")
        direction = "n"
        where_to = str(input("Direction: "))
        if where_to != direction:
            print("Not a valid direction!")
        else:
            position = round((position + 0.1), 1)
    elif position == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = ["n", "e", "s"]
        where_to = str(input("Direction: "))
        if where_to not in direction:
            print("Not a valid direction!")
        elif where_to == "n":
            position = round((position + 0.1), 1)
        elif where_to == "e":
            position = round((position + 1.0), 1)
        elif where_to == "s":
            position = round((position - 0.1), 1)        
    print(position)

#endar í 1.2 sem er rétt