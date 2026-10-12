numbers = [1, 2, 4, 6, 3, 7, 8]
n = 8

total = n * (n + 1) // 2
missing = total

for num in numbers:
    missing -= num

print(missing)

#Test Cases

numbers = [2, 3, 4, 5]
n = 5

total = n * (n + 1) // 2
missing = total

for num in numbers:
    missing -= num

print(missing)

#Time complexity-->O(n)  — we visit each number once.
#Space complexity-->O(1) — we use only a few extra variables.

