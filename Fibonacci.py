lim = int(input("Enter the limit to find the fibonacci: "))


num1=0
num2=1

for i in range(lim):
    print(num1,end=" ")
    result =num1+num2
    num1=num2
    num2=result
    

# lim = int(input("Enter the limit: "))

# num1 = 0
# num2 = 1

# print("Fibonacci series:")

# for i in range(lim):
#     print(num1, end=" ")
#     result = num1 + num2
#     num1 = num2
#     num2 = result

