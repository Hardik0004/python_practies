import json


developer = {
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com"
}
print("Started writing JSON data into a file")
with open("developer.json", "w") as write_file:
    json.dump(developer, write_file) 
print("Done writing JSON data into .json file")