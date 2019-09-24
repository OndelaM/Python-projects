f = open("input.txt","r")
data = f.read()
f.close()
print(data)

lst = [1,2,3,5,6]

def MIN(lst): # Python code to get the minimum element from a list
    return (min(lst)) 
      
Min = min(lst)
print(Min)

def MAX(lst):  # Python code to get the maximum element from a set 
    return (max(lst))

Max = max(lst)
print(Max)

def Average(lst): # Python program to get average of a list 
    return sum(lst) / len(lst) 

avg = Average(lst)
avg = round(avg,2)
print(avg)


ofile = open("output.txt","w")
ofile.write("The min of [1,2,3,5,6] is: 1")
ofile.write("The max of [1,2,3,5,6] is: 6")
ofile.write("The average of [1,2,3,5,6] is: 3.4")
ofile.close()
