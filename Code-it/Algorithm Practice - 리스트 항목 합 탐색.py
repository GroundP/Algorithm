"""
[1, 2, 5, 6, 7, 9, 11] 안에 합이 15가 되는 두 요소의 조합이 있는지 확인하고 싶습니다. 두 요소 6과 9의 합이 15가 되죠? 이 조합이 있는지 없는지를 알고 싶은 거죠.

함수 설명
함수 sum_in_list은 정수 search_sum와 정렬된 정수 리스트 sorted_list를 받아서 sorted_list안의 두 요소의 합이 search_sum가 되는 조합이 있는지 없는지를 불린으로 리턴합니다.

sum_in_list(15, [1, 2, 5, 6, 7, 9, 11])은 불린 True를 리턴합니다.
"""

def sum_in_list(search_sum, sorted_list):
    ''' Brute Force로 풀면 개꿀~
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == search_sum:
                return True
            
    return False
    '''
    start = 0
    end = len(sorted_list) - 1
    
    while start < end:
        mid = (start + end ) // 2
        
        if sorted_list[start] + sorted_list[end] < search_sum:
            start += 1
        elif sorted_list[start] + sorted_list[end] > search_sum:
            end -= 1
        else:
            return True
    
    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))