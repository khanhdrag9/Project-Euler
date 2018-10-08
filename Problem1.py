ranger = 1000

sum = 0

for i in range(3, ranger, 3):
	five = i + 2*i/3
	if(i%3==0):
		sum+=i
	if(five%5==0 and five<ranger and five%3!=0):
		sum+=five

print("Sum : " + str(sum))