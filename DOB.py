names = []
bdays = []

f = open("DOB.txt", "r")
data = f.readlines()

for line in data:
    parts = line.split()
    names.append(parts[:2])  # store the name
    bdays.append(parts[2:])  # store the bday

f.close()

print("Name")
for i, name in enumerate(names, start=1):
    print("{}. {}".format(i, " ".join(name)))

print("Bday")
for i, bday in enumerate(bdays, start=1):
    print("{}. {}".format(i, " ".join(bday)))   





    


