import sys

n, m = map(int,sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            nowx = i
            nowy = j
            break
        
def dfs(x,y):
    global cnt

    if x<0 or y<0 or x>n-1 or y>m-1:
        return
    
    if graph[x][y] == 'I' or graph[x][y] == 'O' or graph[x][y] == 'P':
        if graph[x][y] == 'P':
            cnt +=1
        graph[x][y] = -1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        
cnt = 0        
dfs(nowx,nowy)
if cnt == 0:
    cnt = 'TT'
    
print(cnt)