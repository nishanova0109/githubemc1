#letter n
for i in range (5):
    for j in range (5):
        if j==0 or j==4 or (i==j and j<4):
            print("*",end="")
        else:
            print(" ",end="")
    print(" ",end="")
    #letter i

    for j in range (5):
        if i==0 or j==2 or i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ",end="")
#letter s

    for j in range (5):
        if (i==0 and j!=0) or (i==4 and j!=4) or( j==0 and i==1) or (i==2 and j!=0 and  j<4)  or (i==3 and j==4):
            print("*",end="")
        else:
            print(" ",end="")
    print(" ",end="")
#letter h

    for j in range (5):
         if j==0 or j==4 or i ==2:
             print("*",end="")
         else:
             print(" ",end="")
    print(" ",end="")


    for j in range (5):
        if (i==0 and j!=0 and j!=4) or i==2 or (j==0 and i!=0) or (j==4 and i!=0):
            print("*",end="")
        else:
            print(" ",end="")
   
 
    print() 