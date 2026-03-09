list_1 = ['a','b','c','d','e']
y = 2

for i in range(y):
    last = list_1.pop()     
    list_1.insert(0, last)   

print(list_1)
