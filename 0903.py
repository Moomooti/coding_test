#문제 해결 - 최대 상금

'''
퀴즈 대회에 참가해서 우승하게 되면 보너스 상금을 획득할 수 있는 기회를 부여 받음
우승자는 주어진 숫자판들 중에 두 개를 선택해서 정해진 횟수만큼 서로의 자리를 위치를 
교환할 수 있다.

정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산됨.
숫자판의 오른쪽부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.
*동일한 위치의 교환이 중복되어도 된다.

따라서 정해진 횟수만큼 숫자판을 교환했을 때, 받을 수 있는 가장 큰 금액을 계산해보자.

'''

def dfs(s, k, memo):
    #s =  현재 숫자 리스트
    #K =  남은 교환 횟수
    if k == 0:
        return int(''.join(s)) #최종 금액 반환 ''은 구분자임
    key = (''.join(s),k)
    if key in memo:
        return memo[key]
    max_val = 0
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            s[i], s[j] = s[j], s[i]
            
            max_val = max(max_val, dfs(s, k-1, memo))
            
            s[i], s[j] = s[j], s[i]
    memo[key] = max_val
    return max_val

T = int(input())
for tc in range(1, T+1):
    num_str, k = input().split()
    k = int(k)
    memo = {}
    result = dfs(list(num_str), k, memo)
    print(f"#{tc} {result}")
        
