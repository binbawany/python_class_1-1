#try
#except
#finally
#else

with open("error.txt", "w") as file:
    file.write("This is a sample text.")

try:
    file = open("error.txt", "rt")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: An I/O error occurred.")
else:
    print("File read successfully without any errors.") 
    file.close()
finally:
    print("Execution of the try-except block is complete.")


x = 4

if x <= 0:
    raise Exception("x should be larger than zero.")

else: 
    print("You put a logical number!.")


x = "saad"

if type(x) is int:
    raise TypeError("Value must be in string.")
else:
    print("You put a string value!.")

