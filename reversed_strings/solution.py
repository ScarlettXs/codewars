def solution(string):
    sth = ""
    for i in range(len(string), 0, -1):
        sth += string[i-1]
    return sth