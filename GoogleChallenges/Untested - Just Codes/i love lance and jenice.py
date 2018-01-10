def solution(s):
    answer = []
    for ch in s:
        if ord(ch) <= ord('z') and ord(ch) >= ord('a'):
            ch = chr(ord('z') - ord(ch) + ord('a'))
        answer.append(ch)
    return "".join(answer)


print solution("AabcdEfg")