first = "listen"
second = "silent"

d = {}

for ch in first:
    d[ch] = d.get(ch, 0) + 1

for ch in second:
    d[ch] = d.get(ch, 0) - 1

for value in d.values():
    if value != 0:
        print(False)
        break
else:
    print(True)


#Test Case
first = "hello"
second = "world"

d = {}

for ch in first:
    d[ch] = d.get(ch, 0) + 1

for ch in second:
    d[ch] = d.get(ch, 0) - 1

for value in d.values():
    if value != 0:
        print(False)
        break
else:
    print(True)

