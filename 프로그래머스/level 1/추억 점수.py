def solution(name, yearning, photo):
    answer = [] #결과 저장
    for people in photo: #photo 리스트 각 사진에 대해서
        result = 0 #추억 점수 초기화
        
        for person in people: #사진 속 인물에 대해서
            if person in name: # 인물이 그리운 사람 리스트에 있다면
                index = name.index(person) # 그리운 사람 리스트에서 인물의 인덱스를 찾음
                result += yearning[index] # 추억 점수에 해당 인물의 추억 점수 추가
        
        answer.append(result) # 결과에 추억점수 추가

    return answer #결과 출력