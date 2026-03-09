num = list(map(int, input("Enter numbers: ").split(" ")))
list_even= []
list_odd= []

for i in num:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
        
print("The sum of even numbers is: ",sum(list_even))
print("The sum of odd numbers is: ",sum(list_odd))



