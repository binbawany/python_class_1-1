#string text double quotation marks or single quotation marks. 
greeting = '''Hello, I am Saad.
I am learning 'python',
I want to be an AI engineer for the future'''

print(greeting)

name = 'Saad Qadri' #there are total 10 charectors. all have there indexes. index starts with 0 
name2 = "chicago" #total 20 char. 0-19
age = 38
print(name[5:10]) #starting must be included but ending is excluded
print(name[0:5]) #starting must be included but ending is excluded
print(name2[-7:]) #starting must be included but ending is excluded

print(len(name2)) #len is for length of variable

print("learning" not in greeting) #in keyword is for serching

for x in name2: #loop in string
    print(x)

#slicing
print(name[-5:])#negtive indexing
print(name[:5])#starting from 0 to 4
print(name[0:])#starting from 0 to last
print(name2[0:10:2])#starting from 0 to 9 with step 2
print(name2[::])#starting from 0 to last with step 2
print(name2[::3])#starting from 0 to last with step 3

#modifying string
print(name.upper()) #upper case upper() after varaible name we put .
print(name.lower()) #lower case lower()
print(name.strip()) #remove white space
print(name2.replace("c", "s")) #replace string from chicago c to s
print(name.split(" ")) #split

#concatenation we have to plus two or more string
nameCity = name + " " + name2 #concatenate Saad Qadrichicago
print(nameCity)
print("my name is " + name + "and  my city name is " + name2) #old
print(f"my name is {name}, my age is {19 * 2 * 100 / 100} and my city name is {name2}") #formatting 


#Escape charactors
aim = "My aim is to be a \"Programmer\" \n with \"AI\" Engineer." #\escape charactor
print(aim)


#modulus
s = 25
q = 7

c = s % q
print(c)

