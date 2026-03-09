nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = "PythonSlicing"


data = [10, 20, 30, 40, 50, 60, 70]

print(nums[0:5])
print(nums[7:])
print(nums[1:])
print(nums[:-1])
print(text[0:6])
print(text[6:13])

print(nums[::2])
print(nums[1::3])
print(nums[::-1])
print(nums[2:8:2])

print(text[::2])
print(text[::-1])
print(text[1:10:3])


data = [10, 20, 30, 40, 50, 60, 70]
print(data[-4:])
print(data[:-2])
print(data[4:0:-1])
print(data[4:1:-1])