from enum import Enum

class State(Enum):
    NONE = 0
    INCREASE = 1
    DECREASE = 2

def isIncrease(n1, n2):
    return n2 > n1 and abs(n1 - n2) <= 3

def isDecrease(n1, n2):
    return n2 < n1 and abs(n1 - n2) <= 3

def removeFirst(list: list, element):
    newList = list[:]

    for i, elem in enumerate(newList):
        if elem == element:
            del newList[i]
            break

    return newList

def isSafe(nums: list[int]) -> int:

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

def isSafeRemovingLevels(nums: list[int]) -> bool:
    
    if isSafe(nums):
        return True
    
    for i in range(len(nums)):
        modified_nums = nums[:i] + nums[i + 1:] # Remove one element
        if isSafe(modified_nums):
            return True
        
    return False

with open("input.txt", "r") as file:

    for line in file:
        nums = list(map(int, line.split()))

        if isSafeRemovingLevels(nums):
            amount += 1

print(amount)