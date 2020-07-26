def computepay(h,r):
    ot = 0    
    if(h > 40):
        ot = h - 40
    p = (h-ot)*r + ot*r*1.5
    return p

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate/hrs:"))
pay = computepay(hrs, rate)
print("Pay",pay)