"""
n번째 피보나치 수를 찾아주는 함수 fib_tab을 작성해 보세요.

fib_tab는 꼭 tabulation 방식으로 구현하셔야 합니다!
"""
def fib_tab(n):
    fib_table = [0, 1, 1]
    
    if n <= 2:
        return fib_table[n]
    
    for i in range(3, n+1):
        fib_table.append(fib_table[i-2] + fib_table[i-1])
            
            
    return fib_table[n]
    # 코드를 작성하세요.

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))