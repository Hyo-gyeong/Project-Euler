mlt = 1
mlt_sum = 0
num_sum = 0
for i in range(1,101):
    mlt = (i ** 2)
    mlt_sum += mlt
    num_sum += i
print((num_sum ** 2) - mlt_sum)
