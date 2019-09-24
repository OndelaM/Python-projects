price = input("Enter price of package: ")
price = int(price)
distance = input("Enter total distance in km's: ")
distance = int(distance)
total_of_product = 0
total_of_product+=price


mode_of_transport = input("Which mode of transport do you prefer? (air/freight): ")
if mode_of_transport == "air":
    total_of_product += (distance * 0.36)
        
else:
         total_of_product += (distance * 0.24)

                        
insurance = input("Which insurance do you prefer? (full/limited): ")
full = 50
limited = 25
if  insurance == "full":
    total_of_product+= full
    
    
else:
        total_of_product+= limited

gift = input("Do you prefer a gift? (gift/ no_gift): ")
gift = 15
no_gift = 0
if gift == "gift":
    total_of_product+= gift

delivery_type = input("Which delivery option do you prefer? (priority/standard): ")
priority = 100
standard = 20
if delivery_type == "priority":
    total_of_product+= priority
    
else:
        total_of_product+=standard

print(total_of_product)

        
