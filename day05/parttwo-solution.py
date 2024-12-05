import math


class Rule:
  def __init__(self, first_page, second_page):
    self.first_page = int(first_page)
    self.second_page = int(second_page)

##fileName = "example.txt"
fileName = "input.txt"

is_reading_rules = True
rules = []
updates = []

with open(fileName, 'r') as file:
    num_rows = 0
    for line in file:
        line = line.rstrip()
        if line == "":
            is_reading_rules = False
            continue
        if is_reading_rules:
            line = line.split('|')
            rules.append(Rule(line[0], line[1]))
        else:
            my_list = line.split(",")
            my_list = [int(x) for x in my_list]
            updates.append(my_list)


def check_update(update, rules):
   encountered_pages = []
   rules = [rule for rule in rules if rule.first_page in update and rule.second_page in update]
   for i in range(len(update)):
      current_page = update[len(update) - 1 - i]
      relevant_rules = [rule for rule in rules if rule.first_page == current_page]
      if not have_encountered(relevant_rules, encountered_pages):
        return False
      encountered_pages.append(current_page)
   return True
         
def have_encountered(relevant_rules, encountered_pages):
   for rule in relevant_rules:
       if rule.second_page not in encountered_pages:
          return False
   return True

def order_correctly_get_mid(update, rules):
    rules = [rule for rule in rules if rule.first_page in update and rule.second_page in update]
    new_order = []
    current_index = 0
    while(current_index < len(update)):
        minimum = math.inf
        next_num = 0
        for i in update:
            if i not in new_order:
                num_restrictions = len([rule for rule in rules if rule.first_page == i])
                if num_restrictions < minimum:
                    minimum = num_restrictions
                    next_num = i
            
        new_order.insert(0, next_num)
        current_index += 1

    if(check_update(new_order, rules)):   
        return new_order[math.floor(len(update) / 2)]
    else:
       print("ERROR")

total = 0
for update in updates:
   if not (check_update(update, rules)): 
      result = order_correctly_get_mid(update, rules)
      total += result
         
print(total)