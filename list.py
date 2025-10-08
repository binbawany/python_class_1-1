name = ["saad", "qadri", "chicago"] #list with square bracket. mutable changeable
print(type(name))

#list ordered duplicate
x = [1,2,3,7,5,6,3,4,5] 
print(len(x))

print(x[0]) #indexing start from 0
print(x[-5])
print(x[2:5]) #slicing
if 2 in x:
    print("yes")
else:
    print(f"no {2} is not in list")

x[1] = 20 #modifying list
print(x)

x[1:6] = [10,11,12] #modifying list with slicing
print(x)

x.append(25) #add item at the end only 1 argument
print(x)

x.insert(3, 15) #insert item at any position 3 argument index and value
print(x)

y = [3,35,4]
x.extend(y) #add another list at the end
print(x)

x.remove(4)
print(x)

x.pop(-1)
print(x)

del x[-2]
print(x)

x.clear()
print(x)



#loop repeated actions with number of times in list. for loop & while loop
#block of code more than one line
numbers = [1,2,3,4,5,6,7,8,9,10]
for v in numbers: #after first line there will be a colen
    print(v) #before second line there will be a tab space or 4 spaces


for n in range(len(name)):
    print(name[n])

fruit = ["apple", "banana", "mango", "orange", "grape", "kiwi"]
r = 0
while r < len(fruit):
    print(fruit[r])
    r += 1 #x+=y means x = x + y 

#iterate with index and value with list comprehension

newfruit = [f for f in fruit if "banana" in f]

print(newfruit)

name.sort() #sort in ascending order, alphabetical order
print(name)

newnum = [1,257,4,5,78,35,98,2,3,5]
newnum.sort()
print(newnum)

newnum.sort(reverse=True) #sort in descending order
print(newnum)

mylist = newnum.copy()
print(mylist)

alpha = ["a", "b", "c", "d"]
nume = [1,2,3,4]
combine = alpha + nume
print(combine)

for b in nume:
    alpha.append(b)
print(alpha)

alpha.extend(nume)
print(alpha)

alpha.reverse() #reverse the list
print(alpha)