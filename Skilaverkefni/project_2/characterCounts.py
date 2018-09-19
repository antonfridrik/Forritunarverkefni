sentence = input("Enter a sentence: ")

import string

#byrja að telja á fyrsta bókstaf 0
count_lower = 0
count_upper = 0
count_digits = 0
count_punctuation = 0
punctuations = string.punctuation #!()-[]{};:'"\,<>./?@#$%^&*_~

for letter in sentence:
    if letter.islower():    #lágstafir
        count_lower += 1

for letter in sentence:
    if letter.isupper():    #hástafir
        count_upper += 1

for letter in sentence:
    if letter.isdigit():    #tölur
        count_digits += 1

for letter in sentence:
    if letter in punctuations:  #greinarmerki
        count_punctuation += 1

#Upper case
print("{:>15}".format("Upper case") + "{:>5}".format(count_upper))
#Lower case
print("{:>15}".format("Lower case") + "{:>5}".format(count_lower))
#Digits
print("{:>15}".format("Digits") + "{:>5}".format(count_digits))
#Punctuation
print("{:>15}".format("Punctuation") + "{:>5}".format(count_punctuation))






