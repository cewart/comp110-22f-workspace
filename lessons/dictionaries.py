"""Demonstration of dictionary capabilities."""


# Declaring the type of a dictionary
schols: dict[str,int]

# initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its keu -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value-pair from a dictionary
# By its key.
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

#Update/ Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

#Demonstration of dictionary literals

#Empty dictionary literal
schools = {} #Samw as dict()
print(schools)

# Alternatively initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# WHat happens when a key does not exist
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
print(type(schools[school]))