def merge(list1, list2):
    if len(list1) == 0:
        return list2
    
    if len(list2) == 0:
        return list1
    
    sortlist = []
    idx1 = 0
    idx2 = 0
    
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] < list2[idx2]:
            sortlist.append(list1[idx1])
            idx1 += 1
        elif list1[idx1] > list2[idx2]:
            sortlist.append(list2[idx2])
            idx2 += 1
        else:
            sortlist.append(list1[idx1])
            sortlist.append(list2[idx2])
            idx1 += 1
            idx2 += 1

    if idx2 < len(list2):
        sortlist += list2[idx2:]
            
    if idx1 < len(list1):
        sortlist += list1[idx1:]
    
    return sortlist
    

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    
    mid = len(my_list)  // 2

    leftSide = my_list[:mid]
    rightSide = my_list[mid:]
    
    left = merge_sort(leftSide)
    right = merge_sort(rightSide)
    
    return merge(left, right)
    
# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
