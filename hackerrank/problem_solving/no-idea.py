# disjoint set: 서로소 집합
# 두 수의 최대 공약수가 1이며, 두 수의 일치하는 공약수가 1만 있으면 서로소라 한다.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

answer = 0
for i in array:
    if i in a:
        answer += 1
    elif i in b:
        answer -= 1

print(answer)
