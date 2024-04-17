
# Arithmetic operators.---------------------------------------------------
#Addition (+): Adds two numbers.
#Subtraction (-): Subtracts the right operand from the left operand.
#Multiplication (*): Multiplies two numbers.
#Division (/): Divides the left operand by the right operand (results in a floating-point number).
#Floor Division (//): Divides the left operand by the right operand and rounds down to the nearest whole number.
#Modulus (%): Returns the remainder of the division of the left operand by the right operand.
#Exponentiation ():** Raises the left operand to the power of the right operand.

a=5
b=10
print("sum of a+b :",a+b) #15
print("sub a-b :",a-b) #-5
print("mul a*b :",a*b) #50
print("Div b/a :",b/a) #2
print("Floor Division b//a",b//a) #2
print("modules a%b ",100%12) #reminder 0
print("Exponentiation a**b",2**5)

#Basic Assignment (=): Assigns a value to a variable.
x=5
x*=5
print("x value",x)
#Bitwise Operations in Python::

#Bitwise AND (&): Performs a bitwise AND operation on the binary representations of the operands.
#Bitwise OR (|): Performs a bitwise OR operation.
#Bitwise XOR (^): Performs a bitwise XOR operation.
#Bitwise NOT (~): Flips the bits of the operand, changing 0 to 1 and 1 to 0.
#Left Shift (<<): Shifts the bits to the left by a specified number of positions.
#Right Shift (>>): Shifts the bits to the right.

p = 5  # Binary: 0101
q = 3  # Binary: 0011
result = p & q
print("p&q is :",result)  

# List of Identity Operators
#is: Returns True if both operands refer to the same object.
#is not: Returns True if both operands refer to different objects.
a="hello"
b="mama"
res=a is b
print(res)

#List of Logical Operators :
#AND (and): Returns True if both operands are True.
#OR (or): Returns True if at least one of the operands is True.
#NOT (not): Returns the opposite Boolean value of the operand.

f=True
g=False
r=f or g
print(r)
#Membership Operations in Python
#Membership operators in Python are used to check whether a value is present in a sequence or collection
# such as a list, tuple, or string. The membership operators are "in" and "not in."

#List of Membership Operators
#in: Returns True if the left operand is found in the sequence on the right.
#not in: Returns True if the left operand is not found in the sequence on the right.
a=[1,2,4,5]
res=5 not in a
print(res)

#Relational Operations in Python
#Relational operators in Python are used to compare two values and determine the relationship between them. These operators return a Boolean result, which is either True or False.

#List of Relational Operators
#Equal to (==): Checks if two values are equal.

#Not equal to (!=): Checks if two values are not equal.

#Greater than (>): Checks if the left operand is greater than the right operand.

#Less than (<): Checks if the left operand is less than the right operand.

#Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.

#Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.

