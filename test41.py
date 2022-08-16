star=5

for i in range (0, star):

    for i in range(0,i+1):

      print("*",end=" ")
    
    print("\r")

for i in range(star,0,-1):

    for j in range(0,i-1):

        print("*",end=" ")
    
    print("\r")