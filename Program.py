'''
Codigo sobre Kid Krypto
Antonio Roblero Alejandro Jesús
Rojas Mendez Gabriel
'''
import fileinput

lines = []
for line in fileinput.input(encoding="utf-8"):
    lines.append(line)

#Getting values from input
operation = str.strip(lines[0])
a = int(str.strip(lines[1]))
b = int(str.strip(lines[2]))
A = int(str.strip(lines[3]))
B = int(str.strip(lines[4]))
text = int(str.strip(lines[5]))

#Getting the values of the public and private key
M = a*b-1
e = A*M+a
d = B*M+b
n = (e*d-1)/M

#Discarding numbers that are no longer needed
a = 0
b = 0
A = 0
B = 0
M = 0

#Function to encrypt
def encrypt():
    return int((text*e)%n)

#Function to decrypt
def decrypt():
    return int((text*d)%n)

if operation=="E":
    result = encrypt()
elif operation=="D":
    result = decrypt()

print(result)