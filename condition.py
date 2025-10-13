#if else
a = 50
b = 40

if a < b: #this condition
    print("my condition is true") #execution if condition is true
else:
    print("my condition is false") #execution if condition is true

name = "Muhammad"

if name == "Saad":
    print("Your name is Saad")
else:
    print("Your name is not Saad")

x = 10
y = 2.0

if y > x: #=> greater than or equal to
    print("y is greater than x")
elif y == x: #== equal to
    print("y is equal to x")
elif y < x: #< less than
    print("y is less than x")
else:
    print("None of the conditions are true")


#shorthand if else
age = 19
if age >= 18: print("You are eligible to vote")
else: print("You are not eligible to vote")

print("Eligible to vote") if age >= 18 else print("Not eligible to vote") #more useful

#match statement

day  = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday") 


today = "Friday"
match today:
    case "Monday" | "wednesday":
        print("Today is a python class")
    case "Tuesday" | "Thursday" | "Friday" | "Saturday" | "Sunday":
        print("Today is not a python class but practice day")