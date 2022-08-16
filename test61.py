str = "my favourite fruit is apple"

char_d = dict()

for char in str:

    count = str.count(char)
  
    char_d[char] = count

print('Result:', char_d)