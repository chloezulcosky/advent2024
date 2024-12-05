def IsSafe(count, route):
    isIncreasing = route[count-1] > route[0]
    for i in range(count):
           if(i == 0): continue
           previousItem = route[i-1]
           currentItem = route[i]
           
           # check for increase/decrease
           if((isIncreasing and previousItem > currentItem)
              or (not isIncreasing and currentItem > previousItem)):
               return False
           
           # check for increase/decrease
           diff = abs(previousItem - currentItem)
           if( diff < 1 or diff > 3):
              return False
           
    return True


##fileName = "example.txt"
fileName = "input.txt"

safeRoute = 0

with open(fileName, 'r') as file:
    for line in file:
       str_list = line.strip().split(" ")
       route = [int(x) for x in str_list]
       count = len(route)
       if IsSafe(count, route):
           safeRoute += 1
           

print(safeRoute)
           
