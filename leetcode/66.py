from typing import List


def plusOne(digits: List[int]) -> List[int]:
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        if carry == 1:
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.reverse()
                digits.append(0)
                digits.reverse()
            digits[i] += 1
            carry -= 1
        carry = digits[i] // 10
        digits[i] %= 10
    return digits

print(plusOne([9, 9, 9]))

# best solution
def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9: 
            digits[i] = digits[i] + 1
            return digits
        else: 
            digits[i] = 0

    return [1] + digits

print(plusOne([9, 9, 9]))