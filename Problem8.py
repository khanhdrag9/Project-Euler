import time

#program
n = 4

#get list number for file

text = ""
f = open("P8.txt", "rt")
text = f.read()
f.close()

arrNumber = []
for i in range(len(text)):
	if(text[i] != ' ' and text[i] != '\n'):
		#print (text[i])
		arrNumber.append(int(text[i]))

#print arrNumber;


start = time.time()
#set up
arrResult = [arrNumber[0], arrNumber[1], arrNumber[2], arrNumber[3]]
sub = 0
indexArr = 0

for i in range(n, len(arrNumber)):
	
	sub += (arrResult[indexArr] - arrNumber[i])
	if(sub < 0 ):
		print i + 1
		print arrResult
		sub = 0
		for j in range(indexArr+1):
			arrResult.remove(arrResult[0])
			arrResult.append(arrNumber[i - indexArr])
			indexArr-=1
		indexArr = 0

	elif(indexArr == n - 1):
		indexArr = 0
		sub = 0
	else:
		indexArr+=1

#result
print arrResult
print text.find("9999") 

#end program
end = time.time()
print ("Execute time : %s s" % str(end - start))