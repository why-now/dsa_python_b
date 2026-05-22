import random

def linear_search(values, target):
    for index in range(len(values)):
        if target == values[index]:
            return index
        
    return -1

values = random.sample(range(-10, 1), 5)
print(f"List is {values}")
user_input = int(input("Enter value to search : "))
result = linear_search(values, user_input)
if result > -1:
    print(f"Item {values[result]} found at index {result}")
else:
    print("Not found")