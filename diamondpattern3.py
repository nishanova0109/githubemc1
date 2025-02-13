for i in range(5):
    for j in range(5-i):
        print(" ",end="")
    for m in range (1,2*i):
       
        if m==1 or m==2*i-1:
            print("*",end="")
        elif m%2==0:
            print(" ",end="")
        else:
            print("0",end="")
    print()
for i in range(3,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for m in range (1,2*i):
       
        if m==1 or m==2*i-1:
            print("*",end="")
        elif m%2==0:
            print(" ",end="")
        else:
            print("0",end="")
    print()