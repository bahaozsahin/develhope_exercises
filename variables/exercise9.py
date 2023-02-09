a = 12
b = 'Hello'
print(a, b)

temp = a
a = b
b = temp

del temp

print(a,b)