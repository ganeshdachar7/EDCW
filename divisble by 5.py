div=list(map(int, input("Enter the numbers: ").split()))
length = len(div)

for i in range(length):
   if div[i] % 5 == 0:
        print("The number are divisible by 5 is ",div[i])
    