integer_str = input("Input an integer: ")
integer_int = int(integer_str)

number_str = ""
number_list = ""

for number in range(1,(integer_int + 1)):
    number_str = str(number)
    number_list += number_str
print(number_list[::-2])

#þarf að breyta í string