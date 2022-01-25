def solution(s):
    answer = ''
    string = ''
    dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in s:
        if i.isdigit():
            # 문자열.isdigit() => return True or False
            # 문자열이 포함됐다면 false
            answer += i
        else:
            string += i
            if string in dict.keys():
                answer += str(dict[string])
                string = ''

    return int(answer)


ans = ''
ans = solution('one4seveneight')
print(ans)
