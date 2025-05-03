# Basic examples of operators in Python

# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)       # Addition
print("Subtraction:", a - b)    # Subtraction
print("Multiplication:", a * b) # Multiplication
print("Division:", a / b)       # Division
print("Modulus:", a % b)        # Modulus
print("Exponentiation:", a ** b) # Exponentiation
print("Floor Division:", a // b) # Floor Division

# Comparison Operators
print("Equal:", a == b)         # Equal
print("Not Equal:", a != b)     # Not Equal
print("Greater than:", a > b)   # Greater than
print("Less than:", a < b)      # Less than
print("Greater or Equal:", a >= b) # Greater or Equal
print("Less or Equal:", a <= b) # Less or Equal

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)  # Logical AND
print("Logical OR:", x or y)    # Logical OR
print("Logical NOT:", not x)    # Logical NOT

# Bitwise Operators
print("Bitwise AND:", a & b)    # Bitwise AND
print("Bitwise OR:", a | b)     # Bitwise OR
print("Bitwise XOR:", a ^ b)    # Bitwise XOR
print("Bitwise NOT:", ~a)       # Bitwise NOT
print("Left Shift:", a << 1)    # Left Shift
print("Right Shift:", a >> 1)   # Right Shift

# Assignment Operators
c = 5
c += 2  # Equivalent to c = c + 2
print("Assignment (+=):", c)
c *= 3  # Equivalent to c = c * 3
print("Assignment (*=):", c)

# Membership Operators
lst = [1, 2, 3, 4]
print("In operator:", 3 in lst)  # In operator
print("Not in operator:", 5 not in lst)  # Not in operator

# Identity Operators
d = [1, 2, 3]
e = d
print("Is operator:", d is e)   # Is operator
print("Is not operator:", d is not lst) # Is not operator