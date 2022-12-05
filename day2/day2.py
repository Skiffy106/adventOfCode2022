# Day 1 AdventOfCode 2022
# 12/05/2022
# Mason Tuttle

f = open("day2/input.txt", "r")
# f = open("day2/testcase.txt", "r")
fileInput = f.read()
f.close()

file2dArray = list(map(lambda rawString: rawString.split(" "), fileInput.split("\n")))

# print(file2dArray)

def calculateGameScore(opponent_move, player_move):
  retScore = 0;
  if (player_move == 'X'):
    # player chooses rock
    retScore += 1;
    if (opponent_move == 'A'):
      # opponent chooses rock
      retScore += 3;
    elif (opponent_move == 'B'):
      # opponent chooses paper
      retScore += 0;
    elif (opponent_move == 'C'):
      # opponent chooses scissors
      retScore += 6;
    else:
      print("Error on opponent move!")
  elif (player_move == 'Y'):
    # player chooses paper
    retScore += 2;
    if (opponent_move == 'A'):
      # opponent chooses rock
      retScore += 6;
    elif (opponent_move == 'B'):
      # opponent chooses paper
      retScore += 3;
    elif (opponent_move == 'C'):
      # opponent chooses scissors
      retScore += 0;
    else:
      print("Error on opponent move!")
  elif (player_move == 'Z'):
    # player chooses scissors
    retScore += 3;
    if (opponent_move == 'A'):
      # opponent chooses rock
      retScore += 0;
    elif (opponent_move == 'B'):
      # opponent chooses paper
      retScore += 6;
    elif (opponent_move == 'C'):
      # opponent chooses scissors
      retScore += 3;
    else:
      print("Error on opponent move!")
  else:
    print("Error on player move!")
  return retScore

sumPoints = 0;
for moveArray in file2dArray:
  sumPoints += calculateGameScore(moveArray[0], moveArray[1])

print(sumPoints)