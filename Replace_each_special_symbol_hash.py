import string

str = "/*vishal is @developer & musician!!"
print("The original string is : ", str)

replace_char = '#'

for char in string.punctuation:
    str = str.replace(char, replace_char)

print("The strings after replacement : ", str)
