#Solution: https://pythonandr.com/2015/09/01/highly-divisible-triangular-number-project-euler-problem-12/
from math import *

def divisors(n):
    limit = (int)(sqrt(n))
    divisors_list = []
    for i in range(1, limit + 1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(n/i)
    return len(divisors_list)

def isTriangleNumber(n):
    a = int(sqrt(2*n))
    return 0.5 * a * (a+1) == n

def lastTerm(n):
    if isTriangleNumber(n):
        return int(sqrt(2*n))
    else:
        return None

#number which has 500 divisors
check = 2**4 * 3**4 * 5**4 * 7 * 11

while not isTriangleNumber(check):
    check+=1

seriesLastTerm = lastTerm(check)

while divisors(check) < 500:
    check += seriesLastTerm + 1
    seriesLastTerm += 1

print "Result: " + str(check)


    