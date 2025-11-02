'''Print this pattern:
1
22
333
4444
55555'''
# method-1
n=int(input("Enter no. of rows: "))
i=1
while i<=n:
    print(str(i) * i)

    i+=1

# method-2
n = int(input("Enter no. of rows: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i += 1
