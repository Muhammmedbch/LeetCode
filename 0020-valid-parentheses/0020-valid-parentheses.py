class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        dics = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:

            if char in dics.values():
                stack.append(char)

            else:
                if not stack:
                    return False

                last = stack.pop()

                if last != dics[char]:
                    return False

        return len(stack) == 0