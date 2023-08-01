# Exercise 1: Convert the following dictionary into JSON format
"""
import json
data = {"key1" : "value1", "key2" : "value2"}

jsonData = json.dumps(data)
print(jsonData)
"""
# Exercise 2: Access the value of key2 from the following JSON

# import json

# sampleJson = """{"key1": "value1", "key2": "value2"}"""

# data = json.loads(sampleJson)
# print(data['key2'])

# Exercise 3: PrettyPrint following JSON data
"""
import json
sampleJson = {"key1": "value1", "key2": "value2"}
prettyprint = json.dumps(sampleJson, indent = 2, separators = (",","="))
print(prettyprint)
"""
# Exercise 4: Sort JSON keys in and write them into a file

"""import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("Started writing JSON data into a file")
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")

"""
# Exercise 5: Access the nested key ‘salary’ from the following JSON

# write code to print the value of salary

# import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)
# print(data['company']['employee']['payble']['salary'])

# Exercise 6: Convert the following Vehicle Object into JSON
"""
import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Objdect into JSON")

vehiclejson = json.dumps(vehicle, indent = 4, cls= VehicleEncoder)
print(vehiclejson)

"""

# Exercise 7: Convert the following JSON into Vehicle Object
# Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array