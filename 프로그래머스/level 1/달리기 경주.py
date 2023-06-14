def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} #선수 이름과 인덱스 매핑한 딕셔너리 
    
    for who in callings: # 호출된 선수에 대해 반복문 실행
        idx = result[who] # 호출된 선수의 현재 등수
        result[who] -= 1 # 호출된 선수 등수 -1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1], players[idx] = players[idx], players[idx-1] #호출된 선수와 이전 선수 위치 교환
    return players
    