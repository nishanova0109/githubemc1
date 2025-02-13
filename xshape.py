
for i in range(4,1,-1):
    for j in range(4-i):
        print(" ",end="")
    for m in range (1,2*i):
       
        if m==1 or m==2*i-1:
            print("*",end="")
        
        else:
            print(" ",end="")
    print()
for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for m in range (1,2*i):
        
        if m==1 or m==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    