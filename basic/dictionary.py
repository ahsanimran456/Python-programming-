# Basic dictionary operations and methods in Python

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Accessing values
print("Name:", my_dict["name"])  # Access using key
print("Age:", my_dict.get("age"))  # Access using get() method 

# Adding a new key-value pair
my_dict["profession"] = "Engineer"
print("Updated Dictionary:", my_dict)

# Updating an existing key
my_dict["age"] = 26
print("Updated Age:", my_dict)

# Removing a key-value pair
removed_value = my_dict.pop("city")  # Removes and returns the value
print("Removed City:", removed_value)
print("Dictionary after removal:", my_dict)

# Checking if a key exists
if "name" in my_dict:
    print("Key 'name' exists in the dictionary.")

# Looping over a dictionary
print("\nLooping through keys:")
for key in my_dict:
    print(key)

print("\nLooping through values:")
for value in my_dict.values():
    print(value)

print("\nLooping through key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Dictionary methods
print("\nDictionary Methods:")
print("Keys:", my_dict.keys())  # Returns a view object of keys
print("Values:", my_dict.values())  # Returns a view object of values
print("Items:", my_dict.items())  # Returns a view object of key-value pairs

# Clearing the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)