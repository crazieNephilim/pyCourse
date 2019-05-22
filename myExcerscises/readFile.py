name = raw_input("Enter name: ")
fullPath = "/etc/" + name
f = open(fullPath,"r")
text = f.read()
print(text)
f.close()