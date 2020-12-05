class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        if N == 0: return a
        elif N == 1: return b
        c = None
        for i in range(2, N + 1):
            c = a + b
            a, b = b, c
        return c