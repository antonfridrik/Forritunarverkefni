init_value = input("Initial value: ")
steps = input("Step: ")

steps_int = int(steps)
init_value_int = int(init_value)

count = init_value_int
sum_of_series = 0

while sum_of_series <= 100:
    count += steps_int
    sum_of_series += count
    print(count, end=" ") 

print()
print("Sum of series:",sum_of_series)
#vantar að fyrsta talan komi með í rununa annars rétt