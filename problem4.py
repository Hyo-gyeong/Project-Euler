ifpal= 0
maxnum = 0
for n1 in range(100, 1000):
    for n2 in range(100, 1000):
        mtp = n1 * n2
        txt = str(mtp)
        if (txt == txt[::-1]):
            if (maxnum < mtp):
                ifpal = 1
                maxnum = mtp
                break
print(maxnum)
