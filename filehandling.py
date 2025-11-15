#creating, reading, updating, and deleting files in Python
#open , with open
#"r", read
#"a", append
#"w", write
#"x", create
#"t", text mode
#"b", binary mode
#read(), readline(), readlines()
#write(), writelines()

file = open("myfile.txt", "w")

file.write("Hello, World!\n")
file.write("This is a test file.\n")
file.close()


file = open("myfile.txt", "r")
#print(file.read())
print(file.read(5))

file.close()

with open("myfile.txt", "r") as file:
    print(file.readline())
    print(file.readline())

with open("myfile.txt", "a") as file:
    file.write("Appending a new line.\n")
    file.write("Another appended line.\n")

with open("myfile.txt", "r") as file:
    print(file.read())


with open("saad.py", "w") as command_file:
    command_file.write("print('this is Saad from different file')\n")
    command_file.write("print('Hello from saad.py')\n")

#excute saad.py file with x
import subprocess
subprocess.run(["python3", "saad.py"])


import os
os.remove("myfile.txt")
