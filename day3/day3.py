# Day 3 AdventOfCode 2022
# 12/05/2022
# Mason Tuttle

f = open("day3/input.txt", "r")
# f = open("day3/testcase.txt", "r")
fileInput = f.read()
f.close()

backpackArray = fileInput.split("\n")

# print(backpackArray)

def getPriority(item):
  if (item > 96):
    return item - 96
  else:
    return item - 38

prioritySum = 0
for backpack in backpackArray:
  compartment1, compartment2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
  set1 = set(compartment1)
  set2 = set(compartment2)
  duplicate = set1.intersection(set2).pop()
  prioritySum += getPriority(ord(duplicate))

print(prioritySum)

# ---------- End of Part 1 -------------
# ---------- Begin of Part 2 -----------

prioritySum = 0
for i in range(len(backpackArray)//3):
  set1 = set(backpackArray[i * 3])
  set2 = set(backpackArray[i * 3 + 1])
  set3 = set(backpackArray[i * 3 + 2])
  duplicate = set1.intersection(set2).intersection(set3).pop()
  prioritySum += getPriority(ord(duplicate))

print(prioritySum)

# prioritySum = 0
# for backpack in backpackArray:
#   compartment1, compartment2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
#   set1 = set(compartment1)
#   set2 = set(compartment2)
#   duplicate = set1.intersection(set2).pop()
#   prioritySum += getPriority(ord(duplicate))