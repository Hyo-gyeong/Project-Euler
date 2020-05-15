read_file = open('data.txt', 'r')
write_file = open('bye.txt', 'w')
word = ""
count = 1

while (True):
    line = read_file.readline()
    if not line:
        break
    joined_line = "".join(line.split())
    print(line)
    print(joined_line)

for i in range(1,len(joined_line)):
    if (joined_line[i] == joined_line[i-1]):
        count += 1
    else:
        word = joined_line[i-1] + str(count)
        write_file.write(word)
        count = 1
        
word = joined_line[i-1] + str(count)
write_file.write(word)

read_file.close()
write_file.close()
