# Demonstrating scopes and closures in Python

# def outer_function(outer_variable):
#     def inner_function(inner_variable):
#         # Accessing variables from the outer scope
#         return f"Outer Variable: {outer_variable}, Inner Variable: {inner_variable}"
#     return inner_function

# # Using the closure
# closure_instance = outer_function("I am from outer scope")
# result = closure_instance("I am from inner scope")
# print(result)

# Example of modifying a nonlocal variable in a closure
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Using the counter closure
counter_instance = counter()
print(counter_instance())  # Output: 1
print(counter_instance())  # Output: 2
print(counter_instance())  # Output: 3