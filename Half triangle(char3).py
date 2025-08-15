n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(n,n-i,-1):
        print(chr(k+64),end=" ")
    print("\n")    
