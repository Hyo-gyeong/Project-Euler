ifdecimal = 1
count = 0

while (count < 10001):
    ifdecimal += 1
    for i in range(2, ifdecimal+1):
        if (ifdecimal % i == 0):
            break
    if (ifdecimal == i):
        count += 1

print(count)
print(ifdecimal)
