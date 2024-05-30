n= int(input())
count = 0

MEM = set()
for _ in range(n):
    i = input()
    if i == 'ENTER':
        MEM.clear()
    else :
        if i not in MEM:
            count+=1
        MEM.add(i)
print(count)