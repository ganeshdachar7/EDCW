# #Create a string made of the first, middle and last character
# str = input("Enter the string: ")

# strlen = len(str)

# middle = int(strlen/2)

# out= str[0]

# out = str[middle]
# print(str[0]+out+str[strlen-1])

#Create a string made of the middle three characters
# str =input("Enter the string: ")

# str_length= len(str)
# middle_length=int(str_length/2)

# out=str[middle_length-1:middle_length+2]
# print(out)
#print(str[middle_length-1]+out+str[middle_length+1])

#Append new string in the middle of a given string

# str1= input("Enter the string one: ")
# str2= input("Enter the string two: ")

# str3=str1+str2

# print("The addition of string one and string two is: ",str3)

#Create a new string made of the first, middle, and last characters of each input string

text1= input("Enter the string one: ")
text2= input("Enter the string two: ")

text1_len = len(text1)
text2_len = len(text2)

middle_txt1= int(text1_len/2)
middle_txt2= int(text2_len/2)

print(text1[0]+text2[0]+text1[middle_txt1]+text2[middle_txt2]+text1[-1]+text2[-1])

