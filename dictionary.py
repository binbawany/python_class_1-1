myCar = {
    "brand": "Ford",
    "model": "Mustang Shelby GT 500",
    "year": 2020,
    "color": "red"
}

print(myCar["year"])

print(type(myCar))

myprecar = dict(brand="Toyota", model="Corolla" , year=2020, color="black")

print(myprecar["year"])


print(myCar.keys()) #get all keys
print(myCar.values()) #get all values
print(myCar.items()) #get all items


myCar["year"] = 2021 #change value
print(myCar)

myprecar.update({"year": 2021}) #change value
print(myprecar)

myprecar["price"] = 10000 #add new item
print(myprecar)

myprecar.pop("color") #remove item
print(myprecar)

myprecar.popitem() #remove last item
print(myprecar)