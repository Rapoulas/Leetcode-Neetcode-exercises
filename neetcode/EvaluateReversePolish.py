from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i.isnumeric() or i[0] == "-" and i[1:].isnumeric():
            stack.append(int(i))
        else:
            result = stack[-1]
            stack.pop()
            match (i):
                case "+":
                    result += stack[-1]
                case "-":
                    result = stack[-1] - result
                case "*":
                    result *= stack[-1]
                case "/":
                    result = int(stack[-1] / result)
            stack.pop()
            stack.append(result)
    return stack

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))