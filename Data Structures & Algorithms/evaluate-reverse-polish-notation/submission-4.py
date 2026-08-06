class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = "123456789"
        operations="+-*/"
        stack = []
        for option in tokens:
                num3 = 0
                if option == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = num1+num2
                    stack.append(num3)
                elif option == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = num1-num2
                    stack.append(num3)
                elif option == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = num1*num2
                    stack.append(num3)
                elif option == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = int(float(num1)/num2)
                    stack.append(num3)
                else:
                    stack.append(int(option))
        return stack[0]
            
        