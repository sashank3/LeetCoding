class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # make a res list and stack of same size as input
        # loop through all temps:
        # if a temp is less than stack temp value, pop and keep popping till it no longer is.
        # before each pop, calculate index on main res list and put diff of i - index of stack value

        res = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            while(len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]):
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return res
