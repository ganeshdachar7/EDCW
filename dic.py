# dic = {"Company": "TVS","Model": "Raider", "Make":2025}
# print(dic)

# dic["RTO"]= "Hassan"
# print(dic)
# y=dic.items()
# print(y)

student={"Name":"Anu","Age": 20, "Marks": 85}
print(student)

person = {"name": "Ravi", "city": "Hyderabad", "age": 30}
print(person["city"])

info = {"name": "Kiran", "job": "Engineer"}
info["country"]="India"
print(info)

product = {"item": "Pen", "price": 100}
print(product)
product["price"] = 20
print(product)

data = {"name": "Rahul", "age": 25, "city": "Pune"}
for x,y in data.items():
    print(x,":",y)

user = {"name": "Amit", "phone": 9999999999,"email": "ganesh.d@epiance.com"}
if "email" in user:
    print("The email ID exists")
else:
    print("The email ID does not exists")


emp = {"name": "Sita", "salary": 50000, "role": "HR"}
print(emp)
emp.pop("salary")
print(emp)

d1 = {"x": 2, "y": 4}
d2 = {"y": 5, "z": 6}

for i in d2:
    if i in d1:
        d1[i]+=d2[i]
    else:
        d1[i] = d2[i]

print(d1)


text = "apple banana apple mango banana apple"

words = text.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)

