from collections import defaultdict


def minWindow(s: str, t: str) -> bool:
    if len(s) < len(t):
        return ""
    
    charCount = defaultdict(int)
    for ch in t:
        charCount[ch] += 1
    
    targetCharsRemain = len(t)
    minWin = (0, float("inf"))
    left = 0

    for right, ch in enumerate(s):
        if charCount[ch] > 0:
            targetCharsRemain -= 1
        charCount[ch] -= 1

        if targetCharsRemain == 0:
            while True:
                char_at_start = s[left]
                if charCount[char_at_start] == 0:
                    break
                charCount[char_at_start] += 1
                left += 1
            
            if right - left < minWin[1] - minWin[0]:
                minWin = (left, right)
            
            charCount[s[left]] += 1
            targetCharsRemain += 1
            left += 1
    
    return "" if minWin[1] > len(s) else s[minWin[0]:minWin[1]+1]
        

print(minWindow("OUZODYXAZV", "XYZ"))