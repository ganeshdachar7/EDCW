def Product_Sum(num1, num2):
    product = num1*num2
    if product <= 1000:
        return product
    else:
        return num1+num2
    
result = Product_Sum(20,30)
print("The result is", result)

result= Product_Sum(40,30)
print("The result is", result)

