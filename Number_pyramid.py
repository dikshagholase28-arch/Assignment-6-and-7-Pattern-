n = 5

for i in range(1, n+1):
    print(" " * (n-i), end="")

    for j in range(1, 2*i):
        if j <= i:
            print(i+j-1, end=" ")
        else:
            print(3*i-j-1, end=" ")

    print()