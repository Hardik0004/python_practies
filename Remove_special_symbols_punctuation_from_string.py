import string

str1 = "/* manav is @developer and  & @cricketer"

print("Original string is ", str1)

new_str1 = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str1)