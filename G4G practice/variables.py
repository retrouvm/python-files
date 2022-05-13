#introduction of concepts of variables in Python

age=38
name="ankit"
weight=58.5
print(age)
print(name)
print(weight, "\n")


x=10
y="geek"
z=20
w=z
w=30
print(x, y, z, w, "\n")

is_valid=True
marks=90
pi=3.14
city_name="noida"
print(is_valid)
print(marks)
print(pi)
print(city_name, "\n")

x=None
print(x, "\n")

#SWAP TWO VARIABLES

#using an extra variable
x=100
y=200
temp=x
x=y
y=temp
print(x)
print(y, "\n")

#using comma assignment
x=100
y=200
x,y=y,x
print(x)
print(y,"\n")

#using commas to assign multi values to multi variables
x, y, z=100, "geeks", 10.5
print(x)
print(y)
print(z)
x,y=x-5,y+"for"
print(x)
print(y,"\n")


#ID Function, unique identifier for every object, not variables
print(id(5))
a=10
print(id(a))
b=a
print(id(b))

#literals are stored at the same location if they are the same value
c="geek"
d="geek"
print(id(c))
print(id(d))

#two variables active at the same time in the memory should not have the same identifier
a=10
b=10
print(a is b)
c=a
print(c is b)
c=20
print(c is b, "\n")


#type() function to find out the data type of a variables

#numeric types
a=10
print(type(a))
b=10.5
print(type(b))
c=2+4j
print(type(c))

#none and bool types
a=True
print(type(a))
b=None
print(type(b))

#sequence type->not single items
str="gfg"
print(type(str))
l=[10,20,30]
print(type(l))
t=(10,20,30)
print(type(t))
s={10,20,30}
print(type(s))
d={10:"gfg", 20:"ide"}
print(type(d))