"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

name = 'Supriya'
print('My name is '+name)

print(type(name))

age = 30

print("My age is "+str(age))

height = 5.9

print(height)

factor = age * height

print('My factor '+str(factor))

mycomplex = 5j
print(mycomplex)
mycomp=age + mycomplex
print(mycomp)

print(float(age))
print(complex(age))

x=float(0)
y=int(1)
c=complex(5)

print(x)
print(y)
print(c)
