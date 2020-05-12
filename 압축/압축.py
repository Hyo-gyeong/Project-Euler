rf = open('data.txt', 'r')
wf = open('bye.txt','w')
word = ""
count = 0;

while (True):
    line = rf.readline()
    if not line:
        break
    join_line = "".join(line.split())
    print(line)
    print(join_line)

for i in range(1,len(join_line)):
    if (join_line[i] == join_line[i-1]):
        count += 1
    else:
        word = join_line[i-1] + str(count)
        wf.write(word)
word = join_line[i-1] + str(count)
wf.write(word)

rf.close()
wf.close()

