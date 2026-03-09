
text = "Python Programming"
text1= "Hello"
text2= "Hello123"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.count(text))

print(text[:1])
print(text[:-1])
print(text[0:7])
print(text1[::-1])

print(text2.isalnum())
print(text2.isalpha())
print(text2.isdigit())

text3= "banana"
print(text3.count('a'))

filename="report.pdf"
print(filename.startswith('rep'))
print(filename.endswith('.pdf'))

sentence="i love Java"
print(sentence.replace('Java':'Python'))