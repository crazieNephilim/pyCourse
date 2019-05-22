a = "All People seem to need data processing"

print "***1.*** " + str(len(a))
print "***2.*** " + str(a.find("ata"))
print "***3.*** " + str(a[a.find("ata"):a.find("ata")+3])
word = 'ata'
compare =''
number=0
for letter in a:
    number += 1
    compare += letter
    if len(compare) > len(word):
        compare =  compare[1:]
    if word == compare:
        print "***4.*** " + "Hit at position: " + str(number)

number=len(a)
compare =''
for letter in reversed(a):
    number -= 1
    compare += letter
    if len(compare) > len(word):
        compare =  compare[1:]
    if word == compare:
        print "***5.*** " + "Hit at position: " + str(number)