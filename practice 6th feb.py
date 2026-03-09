#1. Dictionary Frequency
# text =input("Enter the string: ")

# freq={}

# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)



#2. Merge Dictionaries
# d1= {"x": 4, "y":3}
# d2= {"y":4, "z":2}

# result = d1.copy()

# for key, value in d2.items():
#     result[key] = result.get(key,0)+value
# print(result)


#3. Remove Duplicates (Keep Order)

# num = list(map(int, input("Enter numbers: ").split()))

# new_num=[]

# present = set()

# for i in num:
#     if i not in present:
#         new_num.append(i)
#         present.add(i)
# print(new_num)

#Second Highest Number

# num =list(map(int,input("Enter the numbers: ").split()))
# duplicate= list(set(num))
# duplicate.sort()
# print(duplicate[-2])

#Count frequency of each word

# text =input("Enter the string: ")

# low= text.lower().split()

# freq={}

# for i in low:
#     if i in freq:
#         freq[i]= freq[i]+1
#     else:
#         freq[i]= 1
#     # freq[i]=freq.get(i,0)+1

# print(freq)

#2. Find all duplicate elements in a list

# num = list(map(int,input("Enter the number list: ").split()))
# final={}

# for i in num:
#     final[i]= final.get(i,0)+1

# duplicate=[]

# for key,value in final.items():
#     if value > 1:
#         duplicate.append(key)
# print(duplicate)

#Remove duplicates from list (keep order)

# num= list(map(int,input("Enter the numbers: ").split()))

# freq={}

# for i in num:
#     freq[i] = freq.get(i,0)+1

# duplicates= []

# for key, value in freq.items():
#     if value > 1:
#         duplicates.append(key)

# print(duplicates)

#Find second smallest number

# num = list(map(int,input("Enter the numbers: ").split()))

# set_list=list(set(num))
# set_list.sort()

# if len(set_list) < 2:
#     print("Second number is not available")
# else:
#     print(set_list[1])

#Find top 2 highest numbers

# num1=list(map(int,input("Enter the numbers: ").split()))
# num1 = list(set(num1))
# num1.sort()
# print(num1[-2:])


#Merge two dictionaries (add values if same key)

d1={"x":5,"y":4,"z":1}
d2={"x":1,"y":2,"z":2}

result=d1.copy()

for key,value in d2.items():
    result[key]=result.get(key,0)+value

print(result)

#Print characters with count (string compression)















        


    