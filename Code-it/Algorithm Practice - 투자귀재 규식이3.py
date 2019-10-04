"""
이미 sublist_max 함수를 각각 Brute Force과 Divide and Conquer 방식으로 작성했는데요. Brute Force로 풀었을 때는 시간 복잡도가 O(n2), Divide and Conquer를 사용했을 때는 O(nlgn)였습니다.

이번 과제에서는 시간 복잡도를 O(n)로 한 번 더 단축해보세요!

과제 설명은 저번 챕터를 참고하세요!
"""
def sublist_max(profits):
    '''이거 틀림;;'''
    max_profit_so_far = profits[0] # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0] # 가장 끝 요소를 포함하는 구간의 최대 합
    
    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])
        
        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)
    
    return max_profit_so_far

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))