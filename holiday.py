def hotel_cost(n,i): #number of nights is "n"
    cost_hotel = i*int(n)
    return cost_hotel
n = input("Enter the number of nights for hotel stay: ")
i = input("Enter the hotel price: ")

def plane_cost(): 
    
    if c == "CPT":  #city is "c"
        cost_plane = 1111

    elif c == "Durban":
        cost_plane = 899

    elif c == "Johannesburg":
        cost_plane = 999

    return cost_plane

c = input("Enter your destination city (CPT/ Durban/ Johannesburg): ")

def car_rental(d): #number of days is "d"
    rental_car = d * 400
    return rental_car
d = input("Enter the number of days you would like to rent a car: ")


print("Your hotel cost is: R" + str(hotel_cost(n,i)))
print("Your plane cost is: R" + str(plane()))
print("Your car rental is: R" + str(plane(d)))

def holiday_cost(hotel,plane,car):
    total_cost = hotel + plane + car
    return total_cost

hotel = hotel_cost(n,i)
plane = plane_cost()
car = car_rental(d)

print("Total holiday cost is: R" + str(holiday_cost(hotel,plane,cost)))


