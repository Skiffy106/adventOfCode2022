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

# ---------- End of Part 1 -------------
# ---------- Begin of Part 2 -----------

def calculateGameScorePart2(opponent_move, game_end):
  retScore = 0;
  if (game_end == 'X'):
    # game ends in loss
    retScore += 0
    if (opponent_move == 'A'):
      # opponent chooses rock
      # player chooses scissor
      retScore += 3
    elif (opponent_move == 'B'):
      # opponent chooses paper
      # player chooses rock
      retScore += 1
    elif (opponent_move == 'C'):
      # opponent chooses scissors
      # player chooses paper
      retScore += 2
    else:
      print("Error on opponent move!")
  
  elif (game_end == 'Y'):
    # game ends in draw
    retScore += 3
    if (opponent_move == 'A'):
      # opponent chooses rock
      # player chooses rock
      retScore += 1
    elif (opponent_move == 'B'):
      # opponent chooses paper
      # player chooses paper
      retScore += 2
    elif (opponent_move == 'C'):
      # opponent chooses scissors
      # player chooses scissors
      retScore += 3
    else:
      print("Error on opponent move!")
  
  elif (game_end == 'Z'):
    # game ends in win
    retScore += 6
    if (opponent_move == 'A'):
      # opponent chooses rock
      # player chooses paper
      retScore += 2
    elif (opponent_move == 'B'):
      # opponent chooses paper
      # player chooses scissors
      retScore += 3
    elif (opponent_move == 'C'):
      # opponent chooses scissors
      # player chooses rock
      retScore += 1
    else:
      print("Error on opponent move!")
  
  return retScore

sumPoints = 0;
for moveArray in file2dArray:
  sumPoints += calculateGameScorePart2(moveArray[0], moveArray[1])

print(sumPoints)