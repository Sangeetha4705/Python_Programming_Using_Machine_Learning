s=input()
a=int(input())
l=list(s)
for i in range(1,len(l)+1):
    if (i%5==0):
        print(l[i-1],end="")
