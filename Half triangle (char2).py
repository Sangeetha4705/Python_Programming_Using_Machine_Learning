n=int(input())
for i in range(0,n):
    for j in range(0,n-i):
        print(chr(j+65),end=" ")
    print("\n")    
