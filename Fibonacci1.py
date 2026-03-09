range1 = int(input("Enter the range: "))

first= 0
second=1

for i in range(range1): 
    print(first, end=" ")
    first,second=second,first+second