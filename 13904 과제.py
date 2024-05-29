n = int(input())
list_n = []

for _ in range(n):
	day,score = map(int,input().split())
	list_n.append((day,score))
	
list_n.sort()
work = []
n = list_n[-1][0]
ans = 0

for i in range(n,0,-1):
	while list_n and list_n[-1][0] == i:
		work.append(list_n.pop()[1])
		
	work.sort()
	if work:
		ans += work.pop()
	
print(ans)