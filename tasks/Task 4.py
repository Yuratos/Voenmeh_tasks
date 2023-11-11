from functools import lru_cache
@lru_cache()
def reverse_fib_cached (n):
    if n==1 or n==2:
        return 1

    return reverse_fib_cached(n-1) + reverse_fib_cached(n-2)
n = int(input('enter n'))
result = reverse_fib_cached(n)
print(n, '--', result)