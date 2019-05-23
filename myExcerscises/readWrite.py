name = raw_input("Enter name: ")
fullPath = "/home/pythontools/Documents/pyCourse/" + name
f = open(fullPath,"r")
text = f.read()
print(text)
f.close()

f = open(fullPath,"a")
f.write("Line added!")
f.close()