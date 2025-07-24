def isValid(s: str) -> bool:
    stack = []
    brackDict = {"}":"{", "]":"[", ")":"("}

    for i in s:
        if i in brackDict:
            if stack and stack[-1] == brackDict[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

print(isValid("(]"))