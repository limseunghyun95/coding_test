input_pieces = map(int, input().split())

chess_pieces = [1, 1, 2, 2, 2, 8]

result = []
for ip, cp in zip(input_pieces, chess_pieces):
    result.append(cp - ip)

print(' '.join(map(str, result)))
