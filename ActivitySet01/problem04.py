# Conditional Execution


hrs = float(input("Enter Hours:"))
rate = float(input('enter rate'))
if hrs>40:
    pay=(hrs-40)*rate*1.5+40*rate
else:
    pay=hrs*rate

print(pay)