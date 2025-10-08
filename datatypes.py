name = "saad" #string with quotation marks
age = 38 #integer without quotation marks
height = 5.10 #float without quotation marks
is_student = True #boolean without quotation marks, T capital and F capital
my_number = 89j #imaginary

#text string str
my_hobby = "I read books and I love coding in Python."

print(type(my_hobby))

#Numeric type integer int, float, complex j 3j
print(type(age))
print(type(height))
print(type(my_number))

#Sequence type of data
fruit = ["Mango" ,"orange", "banana", "Mango"] #list with square bracket
veg = ("tomato", "potato", "onion") #tuple with round bracket. unmute unchangeable
x = range(6) #range 

print(type(fruit))
print(type(veg))
print(type(x))

#Mapping type
student = {"name": "saad", "age": 38, "height" : 5.10, "is_student" : True} #dictionary KEy value pair dict
print(type(student))

my_set = {"apple", "cherry", "blueberry", "apple"} # set curly bracket. unique 
my_fset = frozenset({"apple", "cherry", "blueberry", "apple"})

print(type(my_set))
print(type(my_fset))


#Boolean
is_human = True #bool

print(type(is_human))

#binary type
hello = b"welcome" #bytes
print(type(hello))

newone = bytearray(5) #byte array
print(type(newone))


second = memoryview(bytes(1)) #memory view
print(type(second))


z = None #None Type
print(type(z))
