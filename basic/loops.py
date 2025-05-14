# # Demonstrating all types of loops and conditions in Python

# # # If-elif-else condition
# # x = 10
# # if x > 15:
# #     print("x is greater than 15")
# # elif x == 10:
# #     print("x is equal to 10")
# # else:
# #     print("x is less than 10")

# # For loop with range
# print("For loop with range:")
# for i in range(1,6):
#     print(i)

# # For loop with a list
# print("For loop with a list:")
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# While loop
# print("While loop:")
# count = 1
# while count < 5:
#     print(count)
#     count += 1

# Nested loops
# print("Nested loops:")
# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}")

# # Break statement
print("Break statement:")
for i in range(10):
    if i == 5:
        break
    print(i)

# # Continue statement
# print("Continue statement:")
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# # Pass statement
# print("Pass statement:")
# for i in range(5):
#     if i == 3:
#         pass  # Placeholder for future code
#     print(i)