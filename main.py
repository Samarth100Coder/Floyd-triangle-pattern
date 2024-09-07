n=int(input("enter a number: "))
a=0
for i in range(n+1):
    for d in range(i):
        a=a+1
        print(a,end=" ")
    print()