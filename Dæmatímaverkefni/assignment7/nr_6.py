# Your function definition goes here

def fibo(n):
    fibonacci = []
    a = 0
    b = 1
    for i in range(n):
        fibonacci.append(a)
        a, b = b, a+b
    return fibonacci

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here 

print(fibo(n))   