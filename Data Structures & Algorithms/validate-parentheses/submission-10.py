class Solution:
    def isValid(self, s: str) -> bool:
        opening_options = "({["
        stack = []
        for char in s:
            if char in opening_options:
                stack.append(char)
            else:
                if (char == ")"):
                    if (len(stack) == 0 or stack[-1] != "("):
                        return False
                    else:
                        stack.pop(-1)
                elif (char == "}"):
                    if (len(stack) == 0 or stack[-1] != "{"):
                        return False
                    else:
                        stack.pop(-1)
                elif (char == "]"):
                    if (len(stack) == 0 or stack[-1] != "["):
                        return False
                    else:
                        stack.pop(-1)
        return len(stack) == 0

            

        