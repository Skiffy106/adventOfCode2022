# Day 1 AdventOfCode 2022
# 12/02/2022
# Mason Tuttle

f = open("day1/input.txt", "r")
# f = open("day1/testcase.txt", "r")
fileInput = f.read()
f.close()

# Splits file into 2d array
elves2dArray = list(map(lambda rawString: rawString.split("\n"), fileInput.split("\n\n")))

# print(elves2dArray)

maxCalories = 0
for calorieArray in elves2dArray:
  elfCalorieSum = 0
  for calories in calorieArray:
    elfCalorieSum += int(calories)
  if elfCalorieSum > maxCalories:
    maxCalories = elfCalorieSum

print(maxCalories)