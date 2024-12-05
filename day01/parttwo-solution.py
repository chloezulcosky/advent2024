##fileName = "example.txt"
fileName = "input.txt"

listOne = []
listTwo = []

with open(fileName, 'r') as file:
   for line in file:
      lists = line.strip().split("   ")
      listOne.append(int(lists[0]) )
      listTwo.append(int(lists[1]) )

similarity = 0
for item in listOne:
   countInListTwo = listTwo.count(item)
   similarity += item * countInListTwo

print(similarity)