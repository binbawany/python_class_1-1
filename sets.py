#set unordered, unindexed, no duplicates, mutable
myset = {"apple", "banana", "cherry", "apple"} #applie duplicated
print(myset) #output will be without duplicate apple

print("banana" in myset)

myset.add("orange")
print(myset)




myset2 = {"mango", "grape"}
myset.update(myset2) #add multiple items
print(myset)

myset.remove("banana") #if item not found will raise error
print(myset)
myset.discard("banana") #if item not found will not raise error
print(myset)

x = myset.pop() #remove random item
print(x)
print(myset)


mysetone = {1,2,3,4,5,6,7}
mysettwo = {5,6,7,8,9,10}

set3 = mysetone.union(mysettwo) #union
print(set3)


mysetone = {1,2,3,4,5,6,7}
mysettwo = {5,6,7,8,9,10}

set3 = mysetone | mysettwo #union
print(set3)


mysetone = {1,2,3,4,5,6,7}
mysettwo = {5,6,7,8,9,10}

mysetone.update(mysettwo) #
print(mysetone)


mysetone = {1,2,3,4,5,6,7}
mysettwo = {5,6,7,8,9,10}

set3 = mysetone.intersection(mysettwo) #intersection
print(set3)

mysetone = {1,2,3,4,5,6,7}
mysettwo = {5,6,7,8,9,10}

set3 = mysetone & mysettwo #intersection
print(set3)


mysetone = {1,2,3,4,5,6,7}
mysettwo = {5,6,7,8,9,10}

set3 = mysettwo.difference(mysetone) #difference
print(set3)

mysetone = frozenset({1,2,3,4,5,6,7})
mysettwo = {5,6,7,8,9,10}

set3 = mysetone - mysettwo #
print(set3)

#frozenset