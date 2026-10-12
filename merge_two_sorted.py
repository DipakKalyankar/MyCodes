a = [1, 4, 7, 10]
b = [2, 3, 8, 11, 15]

result = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result += a[i:]
result += b[j:]

print(result)

#Space Complexity-->O(n+m) because the result list stores all elements from both lists.
