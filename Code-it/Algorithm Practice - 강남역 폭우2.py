"""
강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.

그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.

함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.

예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다. 그러면 0번 인덱스에 높이 3의 건물이, 3번 인덱스에 높이 2의 건물이, 5번 인덱스에 높이 4의 건물이 있다는 뜻입니다. 1번, 2번, 4번 인덱스에는 건물이 없습니다.

그러면 아래의 사진에 따라 총 10 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 10을 리턴하는 거죠.



3차원 말고, 2차원으로 생각해 주세요!
이번에는 파라미터 buildings로 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]가 들어왔다고 합시다. 그러면 아래의 사진에 따라 총 6 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 6을 리턴하는 거죠.



리스트 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
이 정보를 기반으로, trapping_rain 함수를 작성해 보세요!

Brute Force 단원에서는 이 문제를 시간 복잡도 O(n2)로 풀었었는데요, 더 많은 공간을 쓰더라도 조금 더 효율적인 시간 복잡도로 문제를 풀어볼까요?
"""

def trapping_rain(buildings):
    total_height = 0
    max_left = [0] * len(buildings)
    max_right = [0] * len(buildings)
    max_second = -1
    
    # 왼쪽에서 부터 가장 큰 높이
    for i in range(len(buildings)):
        if buildings[i] > max_second:
            max_second = buildings[i]
        max_left[i] = max_second
    
    # 오른쪽에서부터 가장 큰 높이
    max_second = -1
    for i in range(len(buildings)-1, -1, -1):
        if buildings[i] > max_second:
            max_second = buildings[i]    
        max_right[i] = max_second
        
    
    for i in range(1, len(buildings) - 1):
        upper_bound = min(max_left[i], max_right[i])
        total_height += max(0, upper_bound - buildings[i])

    return total_height
    
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))