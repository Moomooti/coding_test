'''

computerAssistant 프로그램에는 작은 오류가 하나 있는데, 바로 이 부분을 약간 손봐야 한다.

for i in range(5):
    number = number * (i +1) // (i+2)
    n = number % 52
    
우리는 입력된 숫자를 다섯 개의 무작위 카드를 추출하는데 쓴다. 문제는, 위와 같은 방법을 
사용할 경우, 추출되는 다섯 개의 카드가 서로 다를 것이라는 보장이없다.
사실 만약 입력한 값이 888888이라면, 추출되는 다섯개의 카든느 이런 순서로 나온다.
['A_C','A_C','7_H','J_D','K_S] 이제 무엇이 문제인지 알아챘을 것이다.
computerAssiant 함수에서 추출되는 카드의 중복 여부를 체크하지 않는다.
이 문제를 수정하기 위해 다섯 개의 서로 다른 카드들이 생성될때까지 카드를 추출을 계속하도록 프로그램을 수종하시오.

'''
number = "입력받는 숫자"

while True:
    cards = []
    num = number
    for i in range(5):
        num = num * (i+1)//(i+2)
        n = num % 52
        cards.append(n)
    if len(set(cards)) == 5: #리스트 카드를 셋 자료형으로 변환하면 중복된 값들은 하나로 합쳐진다. 
        #셋은 집합 자료형으로 수학에서 집합과 동일한 성질을 가짐. 
        #즉 중복을 허용하지 않는 고유한 워소들의 모임이다.
        break

'''

computer Assistant를 수정해서, 만약 같은 기호를 가진 카드들이 두 그룹에 있는 경우,
비밀 카드와 첫 번째 카드 사이에 거리가 더욱 짧은 카드 그룹을 선택해주도록 하세요.
예를 들어 입력된 카드들이 3H(하트), 8H, JC(클로버), KC, 9D(다이아)인 경우,
항상 JC,kC가 비밀 카드와 첫번 째 카드가 되도록 알고리즘을 변경해주세요.


'''

#카드 데이터를 (값,문양) 쌍으로 분리해 저장
#문양별로 그룹화하여 2개 이상의 카드 군이 있는지 확인
#각 그룹 내에서 비밀카드와 첫 번째 카드 간 차이를 계산
#차이가 더 작은 그룹을 선택하여 해당 그룹의 비밀 카드, 첫번째 카드 고정

def parse_card(card):
    value_part = card[:-1]
    suit_part = card[-1]
    
    face_cards = {'J':11, 'Q':12, 'K':13, 'A':1}
    if value_part.isdigit():
        value = int(value_part)
    else:
        value = face_cards.get(value_part, 0)
    return value, suit_part

def choose_closer_group(cards):
    parsed = [parse_card(c) for c in cards]
    
    groups = {}
    for val, suit in parsed:
        groups.setdefault(suit, []).append(val)
        candidate_groups = [vals for vals in groups.values() if len(vals) >= 2]
    if len(candidate_groups) < 2:
        return cards
    
    def distance(group):
        sorted_vals = sorted(group)
        return abs(sorted_vals[1] - sorted_vals[0])
    
    distance = [distance(g) for g in candidate_groups]
    
    min_idx = distance.index(min(distance))
    chosen_group = candidate_groups[min_idx]
    
    chosen_suit = None
    for suit, vals in groups.items():
        if vals == chosen_group:
            chosen_suit = suit
            break
        
    chosen_card = [c for c in cards if c.endswith(chosen_suit)]
    chosen_card_sorted = sorted(chosen_card, key=lambda  c: parse_card(c)[0])
    
    other_cards = [c for c in cards if not c.endswith(chosen_suit)]
    
    final_cards = chosen_card_sorted[:2] + other_cards
    
    return final_cards

cards = ['3H','8H','JC','KC','9D']
result = choose_closer_group(cards)
print(result)

