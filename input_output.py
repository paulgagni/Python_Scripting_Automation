a=eval(input("Enter a value: "))  #eval will always evaluate the data you are entering.  Works with int or float.
b=eval(input("Enter b value: "))
result=a+b
print(f"The value of {a} + {b} = {result}")
print(f"The value of a is: {a} and the type is: {type(a)}")
print(f"The value of b is: {b} and the type is: {type(b)}")