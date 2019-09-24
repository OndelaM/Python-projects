x = int(input("What year do you want to start with?: "))
n = int(input("How many years do you want to check?: "))

for x in range(x,x+n):
    if x%4 == 0 and x%100 != 0 or x%400 == 0:
        print(x, "is a leap year")
    
    elif x%4 != 0:
        print(x, "is not a leap year")

# If a year is divisible by 4, not divisible by 100 and divisible by 400, then it is a leap year
# If a year is not divisible by four, then it cannot be a leap year.
        






    
  
