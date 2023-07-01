def solution(park, routes):
    h = len(park)  # 공원의 행 개수
    w = len(park[0])  # 공원의 열 개수
    for i, p in enumerate(park):  # 공원의 각 행에 대해 반복
        for j, x in enumerate(p):  # 행의 각 열에 대해 반복
            if x == 'S':  # 시작 지점인 'S'를 찾았을 때
                answer = [i, j]  # 시작 지점의 좌표를 answer에 저장
                break  # 시작 지점을 찾았으므로 반복 종료

    for route in routes:  # 이동 경로(routes)에 대해 반복
        a, b = route.split()  # 이동 방향(a)과 거리(b)를 분리하여 저장

        if a == 'E':  # 동쪽으로 이동할 때
            if answer[1] + int(b) < w:  # 이동 후의 열 값이 공원 범위를 넘어가지 않는 경우
                if 'X' not in park[answer[0]][answer[1]:answer[1]+int(b)+1]:  # 이동 경로에 'X'가 없는 경우
                    answer[1] += int(b)  # 열 값을 이동 거리만큼 증가시킴

        elif a == 'W':  # 서쪽으로 이동할 때
            if answer[1] - int(b) >= 0:  # 이동 후의 열 값이 0 이상인 경우
                if 'X' not in park[answer[0]][answer[1]-int(b):answer[1]+1]:  # 이동 경로에 'X'가 없는 경우
                    answer[1] -= int(b)  # 열 값을 이동 거리만큼 감소시킴

        elif a == 'N':  # 북쪽으로 이동할 때
            if answer[0] - int(b) >= 0:  # 이동 후의 행 값이 0 이상인 경우
                if 'X' not in [ch[answer[1]] for ch in park[answer[0]-int(b):answer[0]+1]]:  # 이동 경로에 'X'가 없는 경우
                    answer[0] -= int(b)  # 행 값을 이동 거리만큼 감소시킴

        else:  # 남쪽으로 이동할 때
            if answer[0] + int(b) < h:  # 이동 후의 행 값이 공원 범위를 넘어가지 않는 경우
                if 'X' not in [ch[answer[1]] for ch in park[answer[0]:answer[0]+int(b)+1]]:  # 이동 경로에 'X'가 없는 경우
                    answer[0] += int(b)  # 행 값을 이동 거리만큼 증가시킴

    return answer  # 최종 위치 좌표 반환
