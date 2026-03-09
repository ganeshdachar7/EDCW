Palindrome_Check =input("Enter a string to check Palindrome or not:  " )
Palindrome_Check.lower()



if Palindrome_Check == Palindrome_Check[::-1]:
    print("The given string is Palindrome")
else:
    print("The given string is not a Palindrome")
    