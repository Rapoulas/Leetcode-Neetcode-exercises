from typing import List


def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s: str) -> List[str]:
    res, i = [], 0

    while i < len(s):
        j = i
        while str[j] != "#":
            j += 1
            while str[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res


encode(["we","say",":","yes"])