# Day 4 AdventOfCode 2022
# 12/06/2022
# Mason Tuttle

f = open("day4/input.txt", "r")
# f = open("day4/testcase.txt", "r")
fileInput = f.read()
f.close()

fileArray = fileInput.split("\n")

subsetSum = 0
for i in range(len(fileArray)):
  firstDashIndex = fileArray[i].find("-")
  commaIndex = fileArray[i].find(",")
  secondDashIndex = fileArray[i].rfind("-")
  # print(fileArray[i][0:firstDashIndex], " - ", fileArray[i][firstDashIndex + 1:commaIndex])
  # print(fileArray[i][commaIndex + 1:secondDashIndex], " - ", fileArray[i][secondDashIndex + 1:len(fileArray[i])])
  elf1 = {i for i in range(int(fileArray[i][0:firstDashIndex]), int(fileArray[i][firstDashIndex + 1:commaIndex]) + 1)}
  elf2 = {i for i in range(int(fileArray[i][commaIndex + 1:secondDashIndex]), int(fileArray[i][secondDashIndex + 1:len(fileArray[i])]) + 1)}
  
  if (elf1.issubset(elf2) or elf2.issubset(elf1)):
    subsetSum += 1

print(subsetSum)