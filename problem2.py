f = 1
s = 1
sum = f + s
rslt = 0
while (sum <= 4000000):
	if (sum % 2 == 0):
		rslt += sum
	f = s
	s = sum
	sum = f + s
	
print(rslt)