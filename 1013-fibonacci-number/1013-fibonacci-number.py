class Solution:
    def fib(self, n: int) -> int:

        #base case
        if n in [0,1]:
            return n
        
        else:
            return self.fib(n - 1) + self.fib(n - 2)