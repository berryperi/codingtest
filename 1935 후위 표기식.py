n = int(input())
ex = list(input())
inp = []
num = []
for i in range(n):
    inp.append(int(input()))

for i in ex:
    if 'A' <= i <= 'Z':
        number = ord(i) - ord('A')
        num.append(inp[number])
    else:
        b = num.pop()
        a = num.pop()
        if i == '+':
            num.append(a+b)
        elif i == '-':
            num.append(a-b)
        elif i == '*':
            num.append(a*b)
        elif i =='/':
            num.append(a/b)

print("%.2f" %num[0])