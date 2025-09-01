T = int(input())
for test_case in range(1, T+1) :
    day = int(input())
    prices = list(map(int, input().split()))

max_prices = [0]*day
max_price = prices[-1]
for i in range(day-1, -1, -1) :
    max_price = max(max_price, prices[i])
    max_prices[i] = max_price

benefit = 0
for i in range(day) :
    if max_prices[i] - prices[i] > 0 :
        benefit += (max_prices[i] - prices[i])

print(f'#{test_case} {benefit}')