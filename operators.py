#airthematic operators
#assignment operators
#comparison operators
#logical operators
#identity operators
#membership operators
#bitwise operators

#+ - * / % // **
print(10 + 5)
print(-10+5)
print(10*5)
print(10/5) #float division
print(10//2) #floor division
print(10**3)#10*10*10 exponentiation
print(10%4) #modulus

#assignment operators
x = 5 #x is 5
x += 3 # x = x + 3
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
x = int(x)
x //= 2
print(x)
x **= 3 #3*3*3
print(x)
x %= 5
print(x)
#bitwise operators
a = 10 #1010
b =3 #0011
a &= b #a becomes 0001 = 1 
print(a)
x &= 2
print(x)

x |= 3
print(x)
x ^= 2
print(x)
x >>= 2
print(x)
x <<= 2
print(x)
print(x := 5)
a|=b #a becomes 7 0111
print(a)

#comparision operators
m =5
n=50
m != n
n > m
m < n
n >= m
m <= n
 #logical operators

print(m < n and n > m) #true and true = true
print(m > n or n > m) #true or false = true
print(not(m < n and n > m)) #not true = false orignal reverse