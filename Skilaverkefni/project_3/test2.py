START = 1
END = 10
move_input = ""
r = ""
l = ""

def move_character(direction, start_number): #skilgr. á tilfærslu á x-ás
    if direction == "r":
        start_number += 1
    elif direction == "l":
        start_number -= 1
    else:
        start_number += 0
    return start_number

start_position = int(input("Input a position between " + str(START) + " and " + str(END)+": "))

current_position = start_position #þar byrjum við á x-ásnum

for i in range(START,END+1):
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    move_input = str(input("Input your choice: "))
    if move_input == "r" or move_input == "l":
        if current_position == 1:
            current_position = START
            print("New position is: ",current_position)
            current_position = move_character(move_input, current_position)
        elif current_position == 10:
            current_position = END
            print("New position is: ",current_position)
            current_position = move_character(move_input, current_position)
        else:
            print("New position is:",move_character(move_input, current_position))
            current_position = move_character(move_input, current_position) #setja gildi fyrir næstu loopu
    else:
        print("New position is:",move_character(move_input, current_position))
        break
   
