# Your function definition goes here

def fibo(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here 

print(fibo(n))