s = input()

alphabets = [-1] * 26

for index, element in enumerate(s):
    alphabets_index = ord(element) - 97  # 97 = ord('a')
    if alphabets[alphabets_index] == -1:
        alphabets[alphabets_index] = index

print(' '.join(map(str, alphabets)))
