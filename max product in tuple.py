list1 = [(2,3),(4,5),(1,25)]

first_product= list1[0][0]*list1[0][1]

for i in list1:
    prod= i[0]*i[1]

    if prod > first_product:
        first_product= prod
        higest_tuple=i
    
print(higest_tuple)