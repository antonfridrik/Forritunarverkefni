# is_prime function definition goes here

def is_prime(integer):
    for i in range(2,num):
        if num % i == 0:
            return num, "is not a prime"
        else:
            return num, "is a prime"

num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
print(is_prime(num))