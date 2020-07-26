hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate per Hour"))
overtime = 0

if hrs>40:
    overtime = hrs-40
pay = ((hrs-overtime) * rate) + (overtime * rate * 1.5)
print(pay)
