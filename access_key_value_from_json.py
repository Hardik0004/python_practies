import json

sampleJson = """{"Name" : "Hardik", "Lastname" : "Pansuriya"}"""

data = json.loads(sampleJson)
print(data['Name'])
print(data['Lastname'])