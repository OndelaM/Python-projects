ID = []
ofile = open("RegForm.txt","w")
x = int(input("How many students are registering: "))
ofile.write("Number of students registered")

for i in range(x):
        ID = (input("Please enter your ID number: "))
        ofile.write(ID+"\n")
ofile.close()
