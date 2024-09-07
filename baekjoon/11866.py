n, k = map(int, input().split())

q = [i for i in range(1, n + 1)]

result = []
count = 0
while q:
    v = q.pop(0)
    count += 1
    if count == k:
        result.append(v)
        count = 0
    else:
        q.append(v)

print(f'<{", ".join(map(str, result))}>')
