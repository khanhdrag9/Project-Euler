ranger = 100

#option1:
print "option1 : "
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
sum2 = 0
sumofEndStart = ranger + 1

#1^2 + 2^2 + ... + 10^2 = 385
sum1 = 0
squareofEndStart = ranger*ranger + 1	#10^2 + 1^2
spaceFirst = squareofEndStart - ((ranger-1)*(ranger-1) + 4)	#(10^2 + 1^2) - (9^2 + 2^2)
spaceSecond = squareofEndStart - spaceFirst - ((ranger-2)*(ranger-2) + 9) #(9^2 + 2^2) - (8^2 + 3^2)
space2Space = spaceFirst - spaceSecond

for i in range(ranger/2):
	sum2+=sumofEndStart
	sum1+=squareofEndStart
	squareofEndStart-= spaceFirst;
	spaceFirst-=space2Space

sum2*=sum2
print "Sum of Squares : " + str(sum2)
print "Squares of Sum : " + str(sum1)
print "Difference : " + str(abs(sum2 - sum1))

#option2:
print "\noption2 : "
#(1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4
#1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

sum1 = ranger * (ranger+1) * (2*ranger+1) * 1/6.0
sum2 = ranger*ranger * (ranger+1)*(ranger+1) * 1/4.0
print "Sum of Squares : " + str(sum2)
print "Squares of Sum : " + str(sum1)
print "Difference : " + str(abs(sum2 - sum1))