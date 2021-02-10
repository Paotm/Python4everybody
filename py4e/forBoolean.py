found = False
number = [9,41,12,3,74,15]
print("Before", found)
num = float(input("number: "))

for value in number:
    if value == num:
        found = True
        print(found,value)
print("After",found)        
