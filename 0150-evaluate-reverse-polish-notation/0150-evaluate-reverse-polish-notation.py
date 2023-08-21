class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        symbols = ['+', '-', '*', '/']
        stack = []

        def res(x, y, symbol):
            if symbol == '+':
                return int(x)+ int(y)
            elif symbol == '-':
                return int(x) - int(y)
            elif symbol == '*':
                return int(x) * int(y)
            elif symbol == '/':
                return int(int(x) / int(y))

        for ele in tokens:
            if( stack and ele in symbols):

                y = stack.pop()
                x = stack.pop()
                stack.append(res(x, y, ele))
            
            else:
                stack.append(ele)
        
        return int(stack[0])
