# Your function definition goes here
def count_case(string):
    count_upper = 0
    count_lower = 0
    for letter in string:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1
    return count_upper, count_lower

user_input = input("Enter a string: ")

# Call the function here

u, l = count_case(user_input)
print("Upper case count: ", u)
print("Lower case count: ", l)