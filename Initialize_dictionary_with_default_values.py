employees = ['Hardik', 'Chirag']
defaults = {"designation": 'Developer', "salary": 10000}

res = dict.fromkeys(employees, defaults)
print(res)

print(res["Hardik"])
