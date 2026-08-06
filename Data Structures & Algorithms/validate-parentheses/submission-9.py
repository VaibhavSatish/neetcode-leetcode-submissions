class Solution:
    def isValid(self, s: str) -> bool:
        opening_options = "({["
        stack = []
        for char in s:
            if char in opening_options:
                stack.insert(0, char)
            else:
                if (char == ")"):
                    if (len(stack) == 0 or stack[0] != "("):
                        return False
                    else:
                        stack.pop(0)
                elif (char == "}"):
                    if (len(stack) == 0 or stack[0] != "{"):
                        return False
                    else:
                        stack.pop(0)
                elif (char == "]"):
                    if (len(stack) == 0 or stack[0] != "["):
                        return False
                    else:
                        stack.pop(0)
        return len(stack) == 0

            

        