import json
import pdb
pdb.set_trace()


sampleJson = {"id": 1, "name": "Hardik", "age": 24}

print("Started writing JSON data into a file")

with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)

print("Done writing JSON data into a file")
