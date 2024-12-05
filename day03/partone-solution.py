import re

##fileName = "example.txt"
fileName = "input.txt"

total = 0
with open(fileName, 'r') as file:
    for line in file:
        mults = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
        for m in mults:
            nums =  re.findall(r'[0-9]+', m)
            total += int(nums[0]) * int(nums[1])
            
print(total)