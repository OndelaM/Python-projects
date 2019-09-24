haveLength = False
UpCase = False
lowCase = False
haveNum = False
numCharact = 0
passwordCorrect = False


Length = input("Does the password have 6 characters? (Yes/No): ")
if Length == "Yes":
          haveLength = True
          numCharact +=1

UpperCase = input("Does the password have an upper case? (Yes/No): ")
if UpperCase == "Yes":
          UpCase = True
          numCharact +=1

LowerCase = input("Does the password have a lower case? (Yes/No): ")
if LowerCase == "Yes":
           Upcase = True
           numCharact +=1

Number = input("Does the password have a number (Yes/No)?: ")
if Number == "Yes":
           haveNum = True
           numCharact +=1

if numCharact >= 3:
          passwordCorrect = True
          print("Your password is suitable")

else:
    print("Password error")
