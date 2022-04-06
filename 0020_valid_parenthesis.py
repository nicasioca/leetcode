class Solution:
    def is_valid(self, s: str) -> bool:

        # nothing to match return True
        if s is None:
            return True

        stack = []
        for val in s:
            if val == ')':
                try:
                    current = stack.pop()
                    if current != '(':
                        return False
                except:
                    return False
            elif val == '}':
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif val == ']':
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                if val == '(' or val == '{' or val == '[':
                    stack.append(val)

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.is_valid('{x[x(xx)x]xxx}xxx'))
    