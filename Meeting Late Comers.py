time = input().split()
threshold = (10,00)
count=0
for i in time:
    hours, minutes = map(int,i.split(':'))
    a=(hours,minutes)
    if a>threshold:
        count=count+1
print(count)        


