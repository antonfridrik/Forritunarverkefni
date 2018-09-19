# palindrome function definition goes here

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


in_str = input("Enter a string: ")

# call the function and print out the appropriate message
print(is_palindrome(in_str))