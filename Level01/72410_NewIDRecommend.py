

#   아이디의 길이는 3자 이상 15자 이하여야 합니다.
#   아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
#   단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

#   신규 유저가 입력한 아이디는 new_id라고 가정했을 때,
#   1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
#   2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
#   3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#   4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
#   5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
#   6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#        만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
#   7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


#   문자열 소문자로 변경 str.lower() / 대문자로 변경 str.upper()
#   문자 -> 유니코드 숫자 ord(ch) / 유니코드 숫자 -> 문자 chr(num) --> 문제에서는 사용하지 않았음
#   문자열 찾기 str.find(찾을 문자열) --> 문제에서는 str.replace('..') # 없을 경우 -1
#   문자열 변경 str.replace(찾을 문자열, 변경할 문자열) --> 문제에서는 str.replace('..', '.')
#   맨 앞, 맨 뒤 문자열 제거 str.strip(제거할 문자열) --> 문제에서는 str.strip('.')

#   https://programmers.co.kr/learn/courses/30/lessons/72410


def solution(new_id):
    special_ch = '-_.~!@#$%^&*()=+[{]}:?,<>/'

    # 1단계 : 모든 대문자를 소문자로 변경한다.
    new_id = new_id.lower()

    print("1단계" + new_id)
    # 2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    ans = ''
    for i in range(len(new_id)):
        if new_id[i] in special_ch and new_id[i] not in '-_.':
            continue
        ans += new_id[i]

    print("2단계" + ans)

    # .. 제거
    while(-1 != ans.find('..')):
        ans = ans.replace('..', '.')

    print("3단계" + ans)

    # 앞 끝 . 제거
    ans = ans.strip('.')

    print("4단계" + ans)

    # 16일 때 문자열 자르기
    if len(ans) >= 16:
        ans = ans[0:15].strip('.')
    print("6단계" + ans)

    # 0일 때 a, 2이하일 때 추가
    if len(ans) == 0:
        ans = 'a'

    print("7단계" + ans)

    while len(ans) <= 2:
        ans += ans[-1]

    print("8단계" + ans)

    return ans


final = ''
final = solution("$%^&*1231231hJELIFJASKD^&&**LF")
print("final ID" + final)
