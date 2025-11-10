#function block of code
#define a function
#calling function
#def kyeword
#function name must be in small characters and underscore
#argument/parameter
#return keywordargument for passing the information

#


#defineing a function
def greet(name): #parameter
    print(f"Hello {name}") 
    print(f"How are you? {name}")
    print(f"Goodbye {name}")



#calling function
greet("Saad") #argument


def calculation(name, major, omarks):
    gpa = omarks / 25
    print(f"The Student {name} is in {major} and his gpa is {gpa}")



#calling function
calculation("Saad", "Marketting", 98)

calculation("Muhammad", "Accounting", 70)

calculation("Ammar", "Finance", 85)
calculation("Ali", "HR", 60)


def add(a = 10, b = 5):  #parameter default value, default value is consider when calling the function ius empty
    return a + b


print(add(45, 55))


def pet_animal(animal, name):
    print("I have a ", animal)
    print("My ", animal, "'s name is ", name)


pet_animal(animal="Dog", name="Buddy")  #keyword argument: key value pair
pet_animal("cat", "Kitty")  #positional argument : based on position

#arbitrary arguments
def fruits(*fruits): #star before parameter, means everything *args
    print("I like the following fruits:")
    for fruit in fruits:
        print(fruit)

fruits("Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple" ,"Strawberry")


def student_info(greeting, *info): #single star before parameter
    print(f"I like the student name {info[0]} and {greeting} to all students")


student_info("asslamualikum", "Saad", "Muhammad", "Ammar", "Ali")


def mystu(**stu): #keyword argument **kwargs
    print("his last name is ", stu['last_name'])


mystu(first_name="Saad", last_name="Qadri", age=25, major="Marketing")



#decorators advance python topic
def outer_function(msg):
    def inner_function():
        print("This is inner function and the message is:", msg)
    return inner_function


@outer_function
def decorated_function():
    return "Hello from decorated function"




print(decorated_function())


def changecase(func):
    def innerfunc():
        return func().upper()
    return innerfunc


@changecase
def message():
    return "hello Saad. How is Python going?"

@changecase
def anotherfunc():
    return "this is another function"


print(message())


print(anotherfunc())