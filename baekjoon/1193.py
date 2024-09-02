x = int(input())

line = 1
count = 1
while x > count:
    line += 1
    count += line

index = count - x

if line % 2 == 1:
    print(f'{1 + index}/{line - index}')
else:
    print(f'{line - index}/{1 + index}')
