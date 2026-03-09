list1 = [(1,2),(5,6),(1,2),(3,4)]

seen = set()
result = []

for i in list1:
    if i not in seen:
        result.append(i)
        seen.add(i)

print(result)
