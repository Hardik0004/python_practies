str = "I am 25 years and 10 months old by  august 2022"

print("Original string is", str)

remove_char=[item for item in str if item.isdigit()]

res = "".join(remove_char)

print(res)