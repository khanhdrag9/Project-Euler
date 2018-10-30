import time

start = time.time()
#program
arrPrimary = [2]

def checkPrimaryNumber(n):
	for i in range(len(arrPrimary)):
		if(n%arrPrimary[i]==0):return 0
	arrPrimary.append(n)
	return 1

count = 1
i = 1

while(count!=10001):
	i+=2
	if(checkPrimaryNumber(i)==1):
		count+=1
#end
end = time.time()

print ("Result " + str(i))
print ("Execute time : %s s" % str(end - start))