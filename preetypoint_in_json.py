import json

sampleJson = {"Name": "Hardik", "Lastname": "Pansuriya", "location": "surat"}
prettyPrintedJson = json.dumps(sampleJson, indent=2, separators=(",", " = "))

print(prettyPrintedJson)
