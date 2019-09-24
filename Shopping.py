product1 = input("Enter a product: ")
product2 = input("Enter a second product: ")
product3 = input("Enter a third product: ")

print(product1)
print(product2)
print(product3)

product1_price = float(input("Enter the price of the first product: "))
product2_price = float(input("Enter the price of the second product: "))
product3_price = float(input("Enter the price of the third product: "))

print(product1_price)
print(product2_price)
print(product3_price)


sum = product1_price + product2_price + product3_price
sum = str(round(sum,2))
print(sum)

average = (product1_price + product2_price + product3_price) / 3
average = str(round(average,2))
print(average)

print("The Total price of the products is" + " " + "R" + (sum) + " " + "and the average price of the products is" + " " + "R" + (average))
