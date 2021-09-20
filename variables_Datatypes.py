#***VARIABLES***

a = 10
print(a)

x=4
print(x)
print('x')
print("hello")
y=5.6
print(y)
print(type(x))
print(type(y))

#Re-declare a varliable
x=23
print(x)

#Delete a variable
x=23
print(x)
del x
print(x)   #This is cause error since we deleted the variable: NameError: name 'x' is not defined

#Define variable names
#1. Contain letters, numbers and underscore (You can start with a letter or underscore)
#2. Should not be a keyword (if, print) https://www.w3schools.com/python/python_ref_keywords.asp
#3. Cannot contain spaces
#4. Cannot start with a number
#5. Variables are case sensitive a and A are different variables

x=5
print(id(x))  #View memory location of your variable
id_x=id(x)
print(id_x)

#***DATA_TYPES***
#Every value in Python has a data type
#Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these clases.
#There are various data types in Python

#Basic data types are:
# 1. Numbers (int, float and complex)
# 2. Strings
# 3. Boolean
x=3
y=5.6
z=3+4j
print(x,type(x))
print(y,type(y))
print(z,type(z))

#Car re-write this way, but prints in single line:
x=3;y=5.6;z=3+4j
print(x,y,z)

lang_name="python scripting"
print(lang_name)
my_name="paul"
print(my_name, type(my_name))

#Boolean is either True or False, this is case sensitive
my_value=True
my_new_value=False
my_one_more="True"

print(my_value,type(my_value))  #type=bool
print(my_new_value,type(my_new_value)) #type=bool
print(my_one_more,type(my_one_more)) #type=str
#my_one_more=true  This is display error not defined.  If you use quotes for "True" or False" then it will convert to string.


