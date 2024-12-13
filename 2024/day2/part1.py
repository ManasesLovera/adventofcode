from enum import Enum

class State(Enum):
    NONE = 0
    INCREASE = 1
    DECREASE = 2

def isIncrease(n1, n2):
    if n2 > n1 and abs(n1 - n2) <= 3:
        return True
    return False

def isDecrease(n1, n2):
    if n2 < n1 and abs(n1 - n2) <= 3:
        return True
    return False

def isSafe(line: str) -> int:
    nums = list(map(int, line.split()))

    state = State.NONE
    
    if isIncrease(nums[0], nums[1]):
        state = State.INCREASE
    elif isDecrease(nums[0], nums[1]):
        state = State.DECREASE
    else:
        return False
    
    for i in range(1,len(nums)):

        if state == State.INCREASE and not isIncrease(nums[i-1], nums[i]):
            return False
                
        elif state == State.DECREASE and not isDecrease(nums[i-1], nums[i]):
            return False

    return True

amount = 0

with open("input.txt", "r") as file:

    for line in file:
        amount += 1 * isSafe(line)

print(amount)