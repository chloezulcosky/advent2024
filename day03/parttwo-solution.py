from pathlib import Path
import re

##fileName = "example.txt"
fileName = "input.txt"

locations = {}
do = True

total = 0

file_path = Path(fileName)

file_content = file_path.read_text()

for match in re.finditer(r'mul\([0-9]+,[0-9]+\)', file_content):
    locations[match.start()] = match.group()
for match in re.finditer(r'do\(\)', file_content):
    locations[match.start()] = match.group()
for match in re.finditer(r'don\'t\(\)', file_content):
    locations[match.start()] = match.group()

        

ordered_locations = sorted(locations.keys())
for key in ordered_locations:
    value = locations[key]
    if( value == "do()"): do = True
    elif( value == "don't()"): do = False
    else:
        if do: 
            nums =  re.findall(r'[0-9]+', value)
            total += int(nums[0]) * int(nums[1])
          
print(total)