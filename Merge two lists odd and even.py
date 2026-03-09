# list1 = [21, 20, 30, 30, 45]
# list2 = [41, 35, 46, 24, 58]

# list3 = []

# # odd numbers from first list
# for num in list1:
#     if num % 2 != 0:
#         list3.append(num)

# # even numbers from second list
# for num in list2:
#     if num % 2 == 0:
#         list3.append(num)

# print(list3)


list1= [21, 20, 30,30,45]
list2 =[41,35,46,24,58]

list3=[]

for i in list1:
    if i % 2 == 0:
        list3.append(i)

for i in list2:
    if i % 2 !=0:
        list3.append(i)
print(list3)

