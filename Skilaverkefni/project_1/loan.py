balance = float(input("Input the cost of the item in $: "))

import math

if balance <= 1000.00:
    interest_rate = 1.50/100.00
else:
    interest_rate = 2.00/100.00

month = 0.00
monthly_payment = 50.00
total_months = 0.00
sum_interest = 0.00
    
while balance > 0.00:
    interest_paid = interest_rate * balance #greiddir vextir
    balance += interest_paid #vextir ofaná
    balance -= monthly_payment #eftirstöðvar eftir mánaðarlega greiðslu
    month += 1
    payment = 50.00
    total_months += 1
    sum_interest += interest_paid

    if balance < 0: #síðasta afborgun/línan
        payment = payment + balance 
        balance = 0.0

    print("Month:",int(month), "Payment:",round(payment, 2), "Interest paid:",round(interest_paid, 2), "Remaining debt:",round(balance, 2),)

print("Number of months:",int(total_months))
print("Total interest paid:",round(sum_interest, 2))