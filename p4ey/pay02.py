hrs = input("Enter Hours:")
h = float(hrs)
rate= input("Enter rate:")
r = float(rate)

if h > 40:
   hr = (((h - 40) * 1.5 ) + 40 )
   print(hr * r)
else:
    print(h * r)
    