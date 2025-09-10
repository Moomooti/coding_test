''' 
연습 문제1

여러분은 사실 업무에 치여서 아무떄나 파티에 갈 수 있을 만한 여유가 없습니다. 
여러분들을 위해 직접 함수에 입력변수를 추가해서, 입력값으로 주어지는 시간(ystart시-yend시)
안에서 가장 많은 연예인을 만날 수 있는 시간과 연예인 수를 찾도록 수정해보세요.
입력값으로 주어지는 구간은 [ystart, yend)라고 생각합시다.
즉 여러분은 ystart <= t < yend를 만족하는 시간 t에만 파티에 있습니다.

'''

#함수의 목적
'''
주어진 시간 구간 즉, ystart 이사잉고, yend 미만인 시간들 중에서 가장 많은 연예인을
만날 수 있는 시간과 그 떄의 연예인 수를 찾는다.

'''

def max_celebs_in_time_range(celeb_times, ystart: int, yend: int):
    max_celebs = 0
    time_of_max = ystart
    for t in range(ystart, yend): #내가 이 파티에실제로 머무를 수 있는 시간 범위
        count = 0 
        for start, end in celeb_times:  # 연예인들의 입장시간과 퇴장 시간
            if start <= t < end: # 현재 시간 t가 연예인 입장 시간 이상이고, 퇴장 시간 미만일 때, 그 연예인이 그 시간 파티에 있다.
                count += 1 #연예인 카운트
        if count > max_celebs: # 최대값 갱신 여부 판단
            max_celebs = count
            time_of_max = t
    return (time_of_max, max_celebs)

# 예시 데이터
celebraitons = [
    (1,5),
    (3,7),
    (4,6),
    (6,8),
    (7,10),
    (9,11)
]

# 테스트: 구간 [4, 9)
result = max_celebs_in_time_range(celebraitons, 4, 9)
print(result)  # (4, 3)

'''
연습문제 2

시간 단위에 의존하지 않고, 파티에 갈 수 있는 최적의 시간을 찾는 다른 방법이 있습니다. 
우리가 차례차례 연예인을 한명씩 선택하고, 선택한 연예인의 시작 시간이 얼마나 많은
다른 연예인들의 존재 구간에 포함되는지를 계산해봅시다.

그렇게 해서 가장 많은 다른 연예인이 선택되는 시간을 우리가 파티를 가야할 시간으로 결정합니다.
이 알고리즘을 코드로 구현하고, 정렬에 기반해서 풀었던 우리 알고리즘과 동일한 결과가 나오는지 비교하라.


'''

def max_celebs_in_time_range(celeb_times, ystart, yend):
    max_celebs = 0
    time_of_max = ystart
    for t in range(ystart, yend):
        count = 0
        for start, end in celeb_times:
            if start <= t < end:
                count += 1
        if count > max_celebs:
            max_celebs = count
            time_of_max = t
    return (time_of_max, max_celebs)

def max_celebs_by_start_time(celeb_times): # 연예인 시작 기준 탐색
    max_count = 0
    best_time = None
    for start_candidate, _ in celeb_times: # 연예인 각각의 시작 시간을 후보 시간으로 삼는다. _ 언더스코어는 종료 시간을 무시함.
        count = 0
        for start, end in celeb_times: #시작과 퇴장시간을 하나씩 꺼낸다. 그리고 내가 선택한 시작 시간이 이 구간에 포함되는지 확인한다.
            if start <= start_candidate < end:
                count += 1
        if count > max_count:
            max_count = count
            best_time = start_candidate
    return best_time, max_count

# 결과 비교
result_old = max_celebs_in_time_range(celebraitons, 4, 9)
result_new = max_celebs_by_start_time(celebraitons)
print(result_old, result_new)  # ((4, 3), (4, 3))


'''
연습문제 3

여러분이 파티에서 만날 연예인들에 대해 여러분의 선호도가 있다고 합시다.
3 튜플로 표현할 수 있습니다. ex) (6.0, 8.0,3)입니다.
코드를 수정해서 가장 많은 선호도를 가지는 시간을 찾을 수 있도록 해보세요.


'''

def max_preference_in_time_range(celeb_times, ystart, yend):
    max_pref = 0
    time_of_max = ystart
    for t in range(ystart, yend):
        total_pref = 0
        for start, end, pref in celeb_times:
            if start <= t < end:
                total_pref += pref # pref는 각 연예인의 선호도 값
        if total_pref > max_pref:
            max_pref = total_pref
            time_of_max = t
    return time_of_max, max_pref

# 연예인 예시 12명 스케줄 (입장시간, 퇴장시간, 선호도)
celebraitons = [
    (1, 5, 2),
    (3, 7, 1),
    (4, 6, 4),
    (6, 8, 5),
    (7, 10, 3),
    (9, 11, 2),
    (2, 9, 3),
    (5, 12, 1),
    (6, 10, 4),
    (8, 13, 2),
    (11, 14, 5),
    (12, 15, 3)
]

# 테스트 예시: 구간 [4, 12)
result = max_preference_in_time_range(celebraitons, 4, 12)
print(result)  # (7, 16)
