import random

def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2

        if values[mid] == target:
            return mid
        elif values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

values = random.sample(range(20, 40), 6)
values = sorted(values) # sort the values
print(f"List is {values}")
user_input = int(input("Enter value to search : "))
result = binary_search(values, user_input)
if result != -1:
    print(f"Item {values[result]} found at index {result}")
else:
    print("Not found")
