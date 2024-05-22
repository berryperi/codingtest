answer = []
for i in range(int(input())):
    li = list(input().split())
    if "ChongChong" in li:
        answer.extend(li)
        continue
    for j in li:
        if j in answer:
            answer.extend(li)

print(len(set(answer)))