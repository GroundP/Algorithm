def fib_memo(n, cache):
    if n <= 2:
        return 1
    
    val1 = 0
    val2 = 0
    if n-1 in cache:
        val1 = cache[n-1]
    else:
        val1 = fib_memo(n-1, cache)
    
    if n-2 in cache:
        val2 = cache[n-2]
    else:
        val2 = fib_memo(n-2, cache)
    
    
    val = val1 + val2
    cache[n] = val
    
    return val

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))