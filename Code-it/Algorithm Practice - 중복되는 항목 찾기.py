"""
(N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있습니다. 그렇다면 어떤 수는 꼭 한 번은 반복되겠지요.

예를 들어 [1, 3, 4, 2, 5, 4]와 같은 리스트 있을 수도 있고, [1, 1, 1, 6, 2, 2, 3]과 같은 리스트가 있을 수도 있습니다. (몇 개의 수가 여러 번 중복되어 있을 수도 있습니다.)

이런 리스트에서 반복되는 요소를 찾아내려고 합니다.

중복되는 어떠한 수 ‘하나’만 찾아내도 됩니다. 즉 [1, 1, 1, 6, 2, 2, 3] 예시에서 1, 2를 모두 리턴하지 않고, 1 또는 2 하나만 리턴하게 하면 됩니다.

중복되는 수를 찾는 시간 효율적인 함수를 설계해보세요
"""

def find_same_number(some_list):   
    '''
    # Brute Force 접근법(O(N^2)
    for i in range(len(some_list)):
        for j in range(i+1, len(some_list)):
            if some_list[i] == some_list[j]:
                return some_list[i]
    '''
    
    '''
    # 정렬해서 반복문 한번만 하기(O(NlogN))
    some_list.sort()
    for i in range(len(some_list)-1):
        if some_list[i] == some_list[i+1]:
            return some_list[i]
    '''
    
    # 리스트 or 사전 이용 (O(N)) - 가장 효율
    dict_num = {}
    for i in some_list:
        if dict_num.get(i) == True:
            return i
        
        if dict_num.get(i) == None:
            dict_num[i] = True  

    return 0

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
