#function block of code
#define a function
#calling function
#def kyeword
#function name must be in small characters and underscore
#argument/parameter
#return keyword


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


def add(a, b):
    return a + b


print(add(5, 10))