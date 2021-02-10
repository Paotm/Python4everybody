count = 0
sum = 0
print("Before",count,sum)
number = [9,41,12,3,74,15]
for value in number :
    count = count + 1
    sum = sum + value
    print(count,value,sum)
print("After", count,sum, sum/count)