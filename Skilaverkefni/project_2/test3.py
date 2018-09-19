vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvxzwy"
word_input = "0" #til að geta sett input inní while lykkju
letter_count = 0

while word_input != ".":    #stoppa lykku á "."
    word_input = (input("Enter a word: "))  
    if word_input[0] in vowels:      #ef fyrsti stafur er í vowels
        pig_latin = word_input[0:] + "yay"
    elif word_input[0] in consonants:    #ef fyrsti stafur er í consonants
        for letter in word_input:
            if letter in vowels:
                last_letters = word_input[letter_count:]
            else:
                first_letters = first_letters + letter
            letter_count += 1
        print(word_input[letter_count:] + word_input[:letter_count] + "ay")
    elif word_input == ".":
        pig_latin = ""
    print(pig_latin) 

