name = input("Please enter your name: ")
name = 0
count = 0
e = 0

#e will be used as the input to prompt the programme to exit once the user enters the correct name

while name != "Ondela":
    count += 1 
    name = input("Please enter your name: ")
    if name == "Ondela":
        print("Incorrect attempts:", count)
        e = (input("Your name is CORRECT press e then press enter, to leave this page: "))
        if e:
            break

    
