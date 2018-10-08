#explain : the find number has format : abccba with 3 digit mul
#(999 x 999 = 998001 (6 digits))
#abccba = 100000a + 10000b + 1000c + 100c + 10b + a
#abccba = 100001a + 10010b + 1100c
#abccba = 11(9091a + 910b + 100c)
#use loop to find a,b,c (9->0)

numberFind = 0
for a in range(9, 0, -1):
	for b in range(9, -1, -1):
		for c in range(9, -1, -1):
			p = a*9091 + b*910 + c*100
			for i in range(90, 9, -1):	#999/11 = 90, 100/11 = 9
				if(p%i==0):
					if(p/i > 999):
						break
					else:
						if(numberFind < p *11):numberFind = p * 11

print numberFind
