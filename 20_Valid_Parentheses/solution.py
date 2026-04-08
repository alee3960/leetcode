CLOSE = {')':'(', ']':'[', '}':'{'}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in CLOSE.values():
                stack.append(ch)
            elif ch in CLOSE:
                if not stack or stack.pop() != CLOSE[ch]:
                    return False
        return not stack