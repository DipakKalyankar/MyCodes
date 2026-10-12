#Using a new list
numbers = [0, 1, 0, 3, 12, 0, 5]

non_zero = []
zeros = 0

for num in numbers:
    if num != 0:
        non_zero.append(num)
    else:
        zeros += 1

result = non_zero + [0] * zeros

print(result)


#Modifying the original list
numbers = [0, 1, 0, 3, 12, 0, 5]

position = 0

for num in numbers:
    if num != 0:
        numbers[position] = num
        position += 1

while position < len(numbers):
    numbers[position] = 0
    position += 1

print(numbers)


#1. Using a new list --> Time Complexity = O(n), Space Complexity = O(n)
#2. Modifying the original list --> Time Complexity = O(n), Space Complexity = O(1)
