score = input("Enter Score: ")
score = float(score)

if score >= 1.1 :
    print("Error, Enter a score between 0.0 and 1.0")
    quit()
elif score >= 0.9 :
	print("A")
elif score >= 0.8 :
	print("B")
elif score >= 0.7 :
	print("C")
elif score >=  0.6 :
	print("D")
elif score <  0.6:
	print("F")
    