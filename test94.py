sampleDict = {"Name": "Hardik", "age": 25, "salary": 10000, "city": "Surat"}
keys = ["Name", "salary","city"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)