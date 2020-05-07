num = 600851475143
dn = 2
max = dn
while (dn <= num):
    if (num % dn == 0):
        num /= dn
        max = dn
    dn += 1
print(max)
