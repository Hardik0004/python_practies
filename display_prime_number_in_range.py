start = 25
end = 50

print("Prime Number Between", start, "And", end)

for num in range(start, end):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
