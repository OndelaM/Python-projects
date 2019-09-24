# string to test
sample_str = "google.com"
# count of each element in string  
str_freq = {} 
  
for i in sample_str:
    if i in str_freq: 
        str_freq[i] += 1
    else: 
        str_freq[i] = 1
  
# printing result  
print ("Count of all characters is :\n " +  str(str_freq)) 


