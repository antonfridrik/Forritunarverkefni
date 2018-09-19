START = 1
END = 10
move_input = ""
r = ""
l = ""

def move_character(direction, start_number): #skilgr. á tilfærslu á x-ás
    if direction == "r":
        if start_number > 9:
            start_number == 10 #festist í 10 þar til að gert er "l" og fer þá í 9
        else:
            start_number += 1 #færir upp um 1 ef talan á bili [1,10]
    elif direction == "l":
        if start_number < 2:
            start_number == 1 #festist í 1 þar til að gert "r" og færist þá í tvo
        else:
            start_number -= 1  #færir niður um 1 ef talan á bili [1,10]
    return start_number

start_position = int(input("Input a position between " + str(START) + " and " + str(END)+": "))

current_position = start_position #þar byrjum við á x-ásnum

for i in range(100):
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    move_input = str(input("Input your choice: ")) # right eða left / l og r
    if move_input == "r" or move_input == "l":
        print("New position is:",move_character(move_input, current_position))
        current_position = move_character(move_input, current_position) #setja gildi fyrir næstu loopu
    else: #ef annað en "r" eða "l"
        print("New position is:",move_character(move_input, current_position)) 
        break
        

