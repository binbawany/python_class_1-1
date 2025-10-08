#there are three types of numbers in python
#1. int (integer) - whole numbers, positive or negative, without decimals, of unlimited length.

x = 5
y = -3
z = 0
s = 1234567890123456789012345678901234567890097359843205987325963265

print(type(s))  # Output: <class 'int'>

#2. float (floating point number) - numbers, positive or negative, containing one or more decimals.
a = 3.0 #float
b = -2.5 #float
c = 0.0 #float
d = 645745. #float
g = 2.998e8 #float in scientific notation
print(type(g))  # Output: <class 'float'>

#3. complex - complex numbers are written with a "j" as the imaginary part
m = 3+5j
n = -2j
o = 4.5j
p = 0j

print(type(o))  # Output: <class 'complex'>

#You can convert from one type to another with the int(), float(), and complex() methods:
#convert from int to float:
x = 11    # int
y = float(x) # convert to float
print(y)          # Output: 11.0

#convert from float to int:
a = 5.99   # float
b = int(a)     # convert to int
print(b)          # Output: 5

#convert from int to complex:
p = 4    # int
q = complex(p) # convert to complex
print(q)          # Output: (4+0j)

#convert from float to complex:
m = 3.5    # float
n = complex(m) # convert to complex
print(n)          # Output: (3.5+0j)



