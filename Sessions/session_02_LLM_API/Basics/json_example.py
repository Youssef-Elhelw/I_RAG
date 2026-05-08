import json

# Sample data to be converted to JSON
data = {
    "name": "Ahmed",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "coding"],
    "is_student": False
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data, indent=4)
# indent=4 is used to make the JSON string more readable by adding indentation and newlines.

# Print the JSON string
print("JSON String:")
print(json_string)

print("\n" + "="*50 + "\n")
# ============== Writing JSON File ==============
# save the JSON string to a file
with open("json_sample.json", "w") as json_file:
    json_file.write(json_string)


# ============== Reading JSON File ==============
# Read the JSON string from the file and convert it back to a Python dictionary
with open("json_sample.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Loaded Data from JSON File (Notice it's a dictionary):")
print(loaded_data)

print("\n" + "="*50 + "\n")

# ============== Accessing Data from the Loaded Dictionary ==============
print("Accessing Data from the Loaded Dictionary:")
print(f"Name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"City: {loaded_data['city']}")
print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")
print(f"Is Student: {loaded_data['is_student']}")