input()
N = map(int, input().split())
input()
M = map(int, input().split())
hashmap = {}
for i in N:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for j in M:
    if j in hashmap:
        print(1, end=" ")
    else:
        print(0, end=" ")