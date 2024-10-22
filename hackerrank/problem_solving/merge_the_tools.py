def merge_the_tools(string, k):
    start_index = 0
    end_index = k
    for _ in range(0, len(string), k):
        answer_set = set()
        answer = ''
        for s in string[start_index:end_index]:
            if s not in answer_set:
                answer += s
                answer_set.add(s)
        print(answer)
        start_index += k
        end_index += k


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
