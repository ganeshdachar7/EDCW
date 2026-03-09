#append function
nums = [1, 2, 3]
nums.append(4)
nums.append(10)
nums.append(20)
print(nums)

#clear function
items = ["pen", "pencil", "eraser"]
print(items)
items.clear()
print(items)
print(len(items))

#copy
a = [10, 20, 30]
b = a.copy()
b.append(40)
print(a)
print(b)

#count
nums = [1, 2, 3, 2, 4, 2, 5]
count1= nums.count(2)
print(count1)

#extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#index
colors = ["red", "blue", "green", "blue"]
print(colors.index("blue"))
print(colors.index("green"))

#insert
nums = [10, 20, 40]
nums.insert(2,30)
nums.insert(0,5)
nums.append(50)
print(nums)

#remove
data = ["A", "B", "C", "D"]
data.pop(3)
print(data)
data.pop(1)
print(data)

#remove
nums = [1, 2, 3, 2, 4]
nums.remove(2)
print(nums)

#reverse
letters = ["a", "b", "c", "d"]
print(letters)
letters.reverse()
print(letters)

#sort
nums = [5, 2, 8, 1, 9]
nums.sort()
print(nums)
desc=nums
nums.reverse()
print(nums)

#mixed challenge
numbers = [3, 1, 4, 1, 5, 9, 1]
count_of_num= numbers.count(1)
print(count_of_num)

numbers.remove(1)
numbers.sort()
rever_name=numbers.reverse()
print(rever_name)
numbers.append(10)
print(numbers)







