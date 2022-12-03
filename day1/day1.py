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

# ---------- End of Part 1 -------------
# ---------- Begin of Part 2 -----------
import sys
 
# setting path
sys.path.append('../adventOfCode2022')
from utils.mergesort import *


caloriesPerElf = [None] * len(elves2dArray)
for i in range(len(elves2dArray)):
  elfCalorieSum = 0
  for j in range(len(elves2dArray[i])):
    elfCalorieSum += int(elves2dArray[i][j])
  caloriesPerElf[i] = elfCalorieSum

caloriesPerElf = merge_sort(caloriesPerElf)
lengthOfCPE = len(caloriesPerElf)

# prints sum of top 3 calories
print((caloriesPerElf[lengthOfCPE - 1] + caloriesPerElf[lengthOfCPE - 2] + caloriesPerElf[lengthOfCPE - 3]))