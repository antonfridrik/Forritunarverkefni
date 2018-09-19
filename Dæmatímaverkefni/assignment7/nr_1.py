# find_min function definition goes here
def find_min(first,second):
    if first < second:
        return first
    if first > second:
        return second
    else:
        return first
       
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

# Call the function here
print("Minimum: ", find_min(first,second))