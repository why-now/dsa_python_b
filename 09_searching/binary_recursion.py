import random

def binary_recursion(values, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if target == values[mid]:
        return mid
    elif target > values[mid]:
        return binary_recursion(values, target, mid + 1, high)
    else:
        return binary_recursion(values, target, low, mid - 1)

values = random.sample(range(20, 40), 6)
values = sorted(values) # sort the values
print(f"List is {values}")
user_input = int(input("Enter value to search : "))
result = binary_recursion(values, user_input, 0, len(values) - 1)
if result > -1:
    print(f"Item {values[result]} found at index {result}")
else:
    print("Not found")