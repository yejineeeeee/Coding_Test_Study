def solution(n,m,section):
    answer = painted = 0
    for i in section:
        if i >= painted:
            painted = i + m
            answer += 1
    return answer