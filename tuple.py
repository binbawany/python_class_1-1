#in single variable multiple assignment
#tuples are ordered and unchangeable (immutable) and allow duplicate values
name = ("john", "doe", "jane", "doe") #round bracket
print(type(name))

print(name[2])
print(name[-1])
print(name[1:3]) #slicing


name = list(name) #convert tuple into list
name[2] = "smith" #it will give error because tuple is immutable
print(name)
name = tuple(name) #convert list into tuple
print(type(name))

for c in name:
    print(c)

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 #concatenate two tuples
print(tuple3)
