sample_dict = {"name": "Hardik","age": 25,"salary": 10000,"city": "surat"}
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)