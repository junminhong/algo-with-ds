# 給一個字串，只包含 ()、[]、{}，判斷括號是否匹配正確。
# 例如：

# "()[]{}" → True

# "(]" → False

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("]["))      # False
print(is_valid_parentheses("{[]}"))    # True
