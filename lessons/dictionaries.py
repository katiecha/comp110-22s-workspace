"""Demonstratons of dictionary capabilities."""

# Declaring the tye of a dictionary
schools: dict[str, int]

# Initiaize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictinary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print dictionary literal representation: {'UNC': 19400, 'Duke': 6717, 'NCSU': 26150}
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value paire from a dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])
# KeyError: 'UNCC'

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")