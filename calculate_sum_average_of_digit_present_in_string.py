import pdb
pdb.set_trace()

str = "SKAj2#ds$%J123456789sadcdcqw32E133@#!#@e"
sum = 0
cnt = 0

for char in str:
    if char.isdigit():
        sum += int(char)
        cnt += 1

avg = sum / cnt
print("Sum is:", sum, "Average is ", avg)
