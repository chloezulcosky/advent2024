##fileName = "example.txt"
fileName = "input.txt"

listOne = []
listTwo = []
length = 0

with open(fileName, 'r') as file:
    for line in file:
       lists = line.strip().split("   ")
       listOne.append(int(lists[0]) )
       listTwo.append(int(lists[1]) )
       length += 1

listOne.sort()
listTwo.sort()

total = 0
for i in range(length):
    total += abs(listOne[i] - listTwo[i])

print(total)