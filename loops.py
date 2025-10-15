myvar = 0
while myvar < 10: #infinite
    print(myvar)
    myvar += 1


student = [98, 87, 76,65,54,43,23,32]

for marks in student: #for uninfinity loop 
    if marks < 60:
        print("You are fail")
    else:
        print("You are pass")


programmers = {"Anas": "python", "Ahmed": "Java", "Ali": "Nodejs", "Ammar": "C++"}

for name in programmers:
    print(name)



fruit = "Orange"
for letter in fruit:
    print(letter)


for index in range(10): #break stop the loop continue skip that particular iteration
    if index == 7:
        continue
    print(index)


#nested loop

colors = ["Red", "Yellow", "Green"]
fruits = ["Apple", "Mango", "Orange"]

for color in colors:
    for fruit in fruits:
        print(color, fruit)


for i in range(4):
    for j in range(11):
        print(f"{i} x {j} = {i*j}")