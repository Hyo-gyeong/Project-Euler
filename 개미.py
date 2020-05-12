ant = "1"
new_ant = ""

for i in range(10):
    index = 0
    while (index < len(ant)):
        current = ant[index]
        count = 1
        while ((index + 1) < len(ant) and ant[index+1] == current): #index를 먼저 파악해줘야 같은 숫자인지 파악 가능! 순서 중요!
            count += 1
            index += 1
        new_ant += current + str(count)
        index += 1
    print(new_ant)
    ant = new_ant
    new_ant = ""
