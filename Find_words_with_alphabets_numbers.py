import pdb
pdb.set_trace()

str = "mayank25 is Data scientist50 and0 AI Expert"
print("The original string is : ", str)

res = []
temp = str.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
