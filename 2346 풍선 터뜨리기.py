import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(n):
    p = q.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        q.rotate(-(p[1] - 1))
    else:
        q.rotate(-p[1])