import random               # Import module to generate random numbers
import string               # Import module to work with letters

# Generate a random number of dictionaries (from 2 to 10)
dict_count = random.randint(2, 10)

# Create an empty list to store dictionaries
dict_list = []

# Loop to create each dictionary
for _ in range(dict_count):
    # Generate a random number of keys for the dictionary (from 1 to 5)
    key_count = random.randint(1, 5)

    # Randomly select unique letters for dictionary keys
    keys = random.sample(string.ascii_lowercase, key_count)

    # Create a dictionary with random values from 0 to 100
    d = {key: random.randint(0, 100) for key in keys}

    # Add the generated dictionary to the list
    dict_list.append(d)

# Print generated list of dictionaries
print("Generated list of dicts:")
print(dict_list)

# Create an empty dictionary for the final merged result
result = {}

# Create a helper dictionary to track max values and dict index
tracker = {}

# Loop through dictionaries with their index (starting from 1)
for idx, d in enumerate(dict_list, start=1):
    # Loop through each key-value pair in the dictionary
    for key, value in d.items():
        # If key is not yet tracked or current value is greater
        if key not in tracker or value > tracker[key][0]:
            # Store max value and index of dictionary
            tracker[key] = (value, idx)

# Build final result dictionary
for key, (value, idx) in tracker.items():
    # Check how many dictionaries contain this key
    count = sum(1 for d in dict_list if key in d)

    # If key appears in more than one dictionary
    if count > 1:
        # Rename key with dictionary index
        result[f"{key}_{idx}"] = value
    else:
        # Otherwise keep key as is
        result[key] = value

# Print final merged dictionary
print("Merged dictionary:")
print(result)
