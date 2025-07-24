from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = []
    for i in range(len(temperatures)):
        for j in range(i, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res.append(j-i)
                break
            if j == len(temperatures)-1:
                res.append(0)
    return res
            

print(dailyTemperatures([30,38,30,36,35,40,28]))

#best solution
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0]*len(temperatures)
    stack = [] #pair: [temp: index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i-stackInd)
        stack.append([t, i])
    return res
print(dailyTemperatures([30,38,30,36,35,40,28]))