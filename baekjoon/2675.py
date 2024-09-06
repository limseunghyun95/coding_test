t = int(input().strip())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    result = ''
    for e in s:
        result += e * r

    print(result)
