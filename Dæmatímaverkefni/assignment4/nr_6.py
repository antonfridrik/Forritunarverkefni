top_num = int(input("Upper number for the range: ")) # Do not change this line
 
for num in range(1,top_num+1):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum +=i
    if num == sum:
        print(num)


