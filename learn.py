#Practice Module

#print world
print("Hello Nalu")

#Variable data
x = 5
y = 10
z = 1
p = x + y + z
carname = "Bugatti"

# simple IF statement
if x + y < z:
    print("pass")
else: print("fail")

#adding var x & y
print(x + y)

#variable carname is Bugatti
print(carname)

"""
All of this is comments
could be multiple lines using
"""

# variable P takes x+y+z gives the equation
print(p)

#Global Function
r = "Virtual"

def myfunc():
    #this r var is only called back in myfunction action
    r = "Fantastic"
    print("My Python is " + r)
myfunc()

#so here the var r goes back to basic r not in the myfunction
print("My Python is " + r)

# this data type is INT
w = 5
print(type(w))

#this data type is STR (String)
s = "Hello my Boss Geiko"
print(type(s))
print(s)

#this data is Float (Float isnt whole number broken down by decimal)
a = 17.5
print(type(a))
print(a)

#this data using [""] is LIST
Q = ["apple", "orange", "banana"]
print(type(Q))
print(Q)

#this data type is TUPLE
c = ("this", "that", "there")
print(type(c))
print(c)

#this data is Dictionary
v = {"name" : "Kid", "age" : "30"}
print(type(v))
print(v)

#this data is Boolean
b = True
print(type(b))
print(b)

#no idea what this is
n = bytearray(3)
print(n)
print(type(n))

#data type is Complex
# m = 1g
# print(type(m))

#the data is range
h = range(10)
print(h)
print(type(h))
# testing functions again
def myfunc():
    h = range(5)
    print(type(h))
    print(h)
myfunc()

#data type in functions as set
def myfunc():
    x = {"Don", "Boss", "King"}
    print(x)
    print(type(x))
myfunc()

#data type in functions as bytes
def myfunc():
    x = b"Hello Master"
    print(x)
    print(type(x))
myfunc()

#data type of memory view bytes
def myfunc():
    x = memoryview(bytes(50))
    print(x)
    print(type(x))
myfunc()

#data type none
def myfunc():
    x = None
    print(x)
    print(type(x))
myfunc()


#length data
def myfunc():
    x = "Hello World"
    print(len(x))
myfunc()

#data array
def myfunc():
    x = "Hello World"
    print(x[1])
myfunc()

for x in "banana":
    print(x)

def myfunc():
    for x in "Hawaii":
        print(x)
myfunc()

txt = "The best things in life is free"
print("free" in txt)

def myfunc():
    txt = "The best things in life is free"
    print("Gamer" in txt)
myfunc()

def myfunc():
    x = "yellow"
    print("red" in x)
myfunc()

def myfunc():
    x = "This is the Matrix"
    print(x[5]) # first character in string is 0
myfunc()

def func():
    x = "Matrix has you"
    print(x[1:5])
    print(x[0:6]) # [first character : number in characters]
func()

#Data auto goes to uppercase with var.upper() same for var.lower()
def uppercase():
    x = "Matrix is everywhere"
    print(x.upper())
uppercase()

def lowercase():
    x = "HELLO WORLD"
    print(x.lower())
lowercase()

#The strip() method removes any whitespace from the beginning or the end:
def strip():
    x = "  Hello Boss    "
    print(x.strip())
strip()

#The replace() method replaces a string with another string:
def myfunc():
    x = "The replace will happen"
    print(x.replace("r", "t"))
myfunc()

#there is also split() but we get it already

# new section
# adding strings 
def myfunc():
    x = "Hello"
    p = "slower"
    y = "World"
    c = x + " " + y
    print(c)
myfunc()

def myfunc():
    fruits = ["apple", "banana"]
    if "apple" in fruits:
        print("Yes, apple is a Fruit!")
    else: print("IDK")
myfunc()

def myfunc():
    if 5 == 10 or 4 == 4:
        print("At least one of this is true")
myfunc()

def myfunc():
    if 5 == 10 or 5 == 6:
        print("yes")
    else: print("no")
myfunc()

fruits = ["apple", "bananas", "strawberries"]
fruits.append("orange")
print(fruits)

soaps = ["irish spring", "dove", "old spice"]
soaps.insert(2, "Chanel")
print(soaps)
soaps.remove("Chanel")
print(soaps)
print(len(soaps))


# names = ["Max", "Kamu", "Cy"]
# last_names = ["Draymond", "Gucci", "Americas"]
# names.update(last_names)
# print(names)

car = {
    "brand": "Ford",
    "model": "Ranger",
    "year": 1980
}
print(car)
print(car.get("model"))
car["year"] = 2023
print(car)
car["model"] = "Bugatti"
print(car.get("model"))

zion = {
    "race": "Hawaiian",
    "location": "Maui",
    "age": 30,
}
print(zion)
print(zion)
zion["smart"] = "dumb"
print(zion)


class Person:
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print("Hello {}!".format(self.name))

zion = Person('Zion')
zion.say_hello()


print("Yes") if 5 > 2 else print("No")


def myfunc(*kids):
    print("The youngest child is " + kids[2])
myfunc()





























