def diff(num1, num2):
    return abs(int(num1) - int(num2))

leftList = []
rightList = []

with open("input.txt", "r") as file:
    for line in file:
        cleanLine = line.strip()
        nums = cleanLine.split('   ')
        leftList.append(int(nums[0]))
        rightList.append(int(nums[1]))

result = 0

while(len(leftList) != 0):
    leftMin = min(leftList)
    rightMin = min(rightList)
    result += diff(leftMin, rightMin)
    leftList.remove(leftMin)
    rightList.remove(rightMin)

print(result)