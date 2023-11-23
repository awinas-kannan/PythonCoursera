import json

person = {
    'first_name': 'Mark',
    'last_name': 'abc',
    'age': 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

json_object = json.dumps(person, indent=10)
with open("person_1.json", "w") as outfile:
    outfile.write(json_object)

####Reading JSON to a File

print('*********Reading JSON to a File############')
with open('person_1.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

print(json_object)
print(type(json_object))
