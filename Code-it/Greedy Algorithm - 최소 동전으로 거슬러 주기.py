"""
최소 동전으로 돈을 거슬러 주는 함수를 Greedy Algorithm으로 구현해 보겠습니다.

우리가 작성할 함수 min_coin_count는 거슬러 줘야 하는 총액 value와 동전 리스트 coin_list를 파라미터로 받고, 거슬러 주기 위해 필요한 최소 동전 개수를 리턴합니다.

예를 들어 1170원을 거슬러 주기 위해서는 500원 2개, 100원 1개, 50원 1개, 10원 2개를 줄 수 있기 때문에 6을 리턴하면 되겠죠?

동전의 조합은 항상 500원, 100원, 50원, 10원이라고 가정합시다.
"""
def min_coin_count(value, coin_list):
    count = 0
    max_list = []
    
    while len(coin_list) > len(max_list):
        max_val = 0
        for i in coin_list:
            if i in max_list:
                continue
                
            max_val = max(max_val, i)
        
        max_list.append(max_val)
        
        count += value // max_val
        value = value % max_val
        
    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))