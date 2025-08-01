def checkInclusion(s1: str, s2: str) -> bool:
    copys1 = sorted(s1)
    for i in range(len(s2)-len(s1)+1):
        copys2 = sorted(s2[i:i+len(s1)])
        if copys1 == copys2:
            return True
    return False

print(checkInclusion("adc", "dcda"))

#best solution
def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = {}
    s2_count = {}

    for i in range(len(s1)):
        s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
        s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

    if s1_count == s2_count:
        return True

    left = 0
    for right in range(len(s1), len(s2)):
        s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)
        s2_count[s2[left]] -= 1

        if s2_count[s2[left]] == 0:
            del s2_count[s2[left]]

        left += 1

        if s1_count == s2_count:
            return True

    return False