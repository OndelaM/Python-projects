import math

P = (int(input("Enter  the amount you would like to deposit: ")))
i = (int(input("Enter the interest rate: ")))
t = (int(input("Enter the number of years of the interest rate: ")))
r = float(i / 100)
interest = input("Do you want simple or compound interest?: ")
CI = P*pow((1+r),t)
CI = float(round(CI,2))
SI = P*(1+r*t)


if interest == "compound":
    print("Compound interest is R",CI)

elif interest == "simple":
        print("Simple interest is R",SI)
    
