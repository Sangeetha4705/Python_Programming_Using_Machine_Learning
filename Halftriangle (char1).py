n=int(input())
for i in range(1,n+1):
    for j in range(0,n+1-j):
        print(chr(j+65),end=" ")
    print("\n")    
