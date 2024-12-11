from typing import List

def appears(num: int, list: List[int]):
    return list.count(num)

leftList = []
rightList = []

with open("input.txt", "r") as file:
    for line in file:
        cleanLine = line.strip()
        nums = cleanLine.split('   ')
        leftList.append(int(nums[0]))
        rightList.append(int(nums[1]))

result = 0

for num in leftList:
    result += num * appears(num, rightList)

print(result)