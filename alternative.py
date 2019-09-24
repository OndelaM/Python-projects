s = "Hello World"
r = [""] * len(s)
r[::2], r[1::2] = s[::2].upper(), s[1::2].lower()
r = "".join(r) 
print(r)

