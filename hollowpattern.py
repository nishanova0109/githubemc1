n = 4  # Number of rows

for i in range(1, n + 1):
    # First loop: Print leading spaces
    for j in range(n - i):
        print(" ", end="")

    # Second loop: Print the star and numbers
    for k in range(1,2*i):
        if k ==1 or k==2*i-1 or i==4 :  # Odd index: print star
            print("*", end="")
        else:  # Even index: print zero
            print(" ", end="")

    # Third loop: Move to the next line
    print()  