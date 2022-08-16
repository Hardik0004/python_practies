import json
import pdb
pdb.set_trace()


sampleJson = """[ 
   { 
      "id":1,
      "Name":" Hardik",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "Name":"Chirag",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('N ame') for item in data]
print(dataList)