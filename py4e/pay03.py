
def computepay(h,r):
    if h > 40:
        hr = (((h - 40) * 1.5 ) + 40 )
        return hr * r
    else :
        return h * r

hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
h = float(hrs)
r = float (rate)


p = computepay(h,r)
print("Pay",p)