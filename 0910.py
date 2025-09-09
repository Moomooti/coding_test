'''
배운 알고리즘: 압축 알고리즘 중 하나인 run-legth encoding

같은 값이 연속해서 나타나는 데이터를 그 값과 반복 횟수로 표현하여 압축하는
비손실 압축 방법이다. 

'''

#연습문제1
#pleaseConfrom(cap1)을 실행하면 나오는 결과에서 한 가지 거슬리는 부분이 있습니다.
#People in positions 2 through 4 flip your caps!
#People in positions 6 through 8 flip your caps!
#People in positions 11 through 11 flip your caps!
#마지막 요청 내용은 사실 다음과 같이 나와야 정확합니다.
#person at position 11 flip your cap!
#좀 더 자연스러운 문장이 나오도록 수정해주세요

def pleaseConfrom(cap1):
    for start, end in cap1:
        if start == end:
            print(f"person at position {start} flip your cap!")
        else:
            print(f"people in positions {start} through {end} flip your caps!")

'''
이렇게 하면 끝 범위가 시작과 같아 한 명만 해당할 때 자연스러운 단수형 문장 출력
'''

#연습문제2
#연습1에서 했던 것처럼, pleaseConformOnePass를 수정해서 자연스러운 문장이 나오도록하고,
#또한 비어있는 입력 리스트가 들어와도 오류가 나지 않도록 해주세요.
#힌트: 구간의 시작을 따로 저장해야하고, 6번째 줄에서 미리 print 함수를 쓰지 않아야 합니다.

def pleaseConformOnePass(cap1):
    if not cap1:
        return  # 빈 리스트일 때 함수 종료
    
    start = cap1[0]
    end = cap1[0]
    
    for pos in cap1[1:]:
        if pos == end + 1:
            end = pos
        else:
            # 구간 출력
            if start == end:
                print(f"person at position {start} flip your cap!")
            else:
                print(f"People in positions {start} through {end} flip your caps!")
            start = end = pos
    
    # 마지막 구간 출력
    if start == end:
        print(f"person at position {start} flip your cap!")
    else:
        print(f"People in positions {start} through {end} flip your caps!")

#연습문제 3번
#머리를 한 껏 꾸미고 와서 모자를 쓸 수 없는 사람들도 있습니다.
#그런 사람들은 H라고 문자로 표현하겠습니다. 그래서 3번째 입력 리스트로 다음과 같은 리스트가 있습니다.
'''
cap3 = ['F','F','B',H','F','B',B','B','F','H','F','F']

'''

#그래서 우리는 H를 가진 사람들은 모두 요청하지 않고 넘어가고 싶습니다.

def pleaseConformSkipH(cap_list):
    positions = []
    # 'H'가 아닌 위치 인덱스(1-based)를 추출
    for i, cap in enumerate(cap_list, start=1): #enumerate: 파이썬 내장 함수로, 반복 가능한 객체를 순회하면서 각 요소의 인덱스와 값을 같이 반환한다.
        if cap != 'H':
            positions.append(i)
            
    if not positions:
        return
    
    start = positions[0]
    end = positions[0]
    
    for pos in positions[1:]:
        if pos == end + 1:
            end = pos
        else:
            if start == end:
                print(f"person at position {start} flip your cap!")
            else:
                print(f"People in positions {start} through {end} flip your caps!")
            start = end = pos
            
    if start == end:
        print(f"person at position {start} flip your cap!")
    else:
        print(f"People in positions {start} through {end} flip your caps!")

cap3 = ['F','F','B','H','F','B','B','B','F','H','F','F']
pleaseConformSkipH(cap3)

#연습문제 4번
#런렝스 인코딩/디코딩을 구현하는 프로그램을 만들어보자.
#예를 들어 입력 문자열 BWWWWWBWWWW가 주어지면, 그것을 줄여서
#1B5W1B4W로 변환해서 출력해야합니다.
#디코딩 함수는 압축된 입력 문자열을 받아서 원래 문자열로 복원시켜야 합니다. 
#압축과 압축 해제를 문자열을 딱 한번만 훑고 지나가면서 결과를 만들어야 한다.

def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    prev_char = s[0]
    
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(str(count))
            result.append(prev_char)
            prev_char = char
            count = 1
    # 마지막 문자 처리
    result.append(str(count))
    result.append(prev_char)
    
    return ''.join(result)

def run_length_decode(s):
    result = []
    count_str = ''
    for char in s:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            result.append(char * count)
            count_str = ''
    return ''.join(result)

# 예시 실행
input_str = "BWWWWWBWWWW"
encoded = run_length_encode(input_str)
decoded = run_length_decode(encoded)

print("Encoded:", encoded)  # 출력: 1B5W1B4W
print("Decoded:", decoded)  # 출력: BWWWWWBWWWW
