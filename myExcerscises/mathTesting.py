# Modules
import math

# Header
print("This is a Math testing program")

# Testing
test = 9 % 5
print("Test=", test, "\tModulo")
test = 9 / 5
print("Test=", test, "\tDivision")
test = 9 * 5
print("Test=", test, "\tMultiplication")
test = round(2.1)
print("Test=", test, "\tRounded")
test = math.floor(2.1)
print("Test=", test, "\tRounded on low")
test = math.ceil(2.1)
print("Test=", test, "\tRounded on high")
test = math.pi
print("Test=", test, "\tPi value")
test = math.sin(math.pi)
print("Test=", test, "\tSinus value of Pi")
test = math.floor(math.sin(math.pi))
print("Test=", test, "\tRounded on low Sinus value of Pi")
test = math.cos(0)
print("Test=", test, "\tCosinus value of Pi")
test = math.asin(0)
print("Test=", test, "\tAsinus value of Pi")
test = math.acos(0)
print("Test=", test, "\tAcosinus value of Pi")
test = math.hypot(3, 4)
print("Test=", test, "\tPitagoras theorem of Right angle triangle (a2 + b2)")
test = math.pow(2, 3)
print("Test= ", test, "\tPower via module")
test = 2 ** 3
print("Test=", test, "\tPower straith")
test = math.exp(2)
print("Test=", test, "\tExp")
test = math.log(27, 3)
print("Test=", test, "\tLog")
