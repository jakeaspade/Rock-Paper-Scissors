import random
choices = ['Rock!', 'Paper!', 'Scissors!']
cpuScore = 0
playerScore = 0
def loss():
  print('Round lost!')
def win():
  print('Round win!')
def tie():
  print('Round Tie!')
while playerScore < 5 and cpuScore < 5:
  print (str(playerScore) + ' to ' + str(cpuScore))
  cpuGuess = choices[random.randint(0,2)]
  guess = input('Rock (r), Paper(p), or Scissors(s):')
  
  if guess == 'rock' or guess == 'r':
    print("I guessed " + cpuGuess)
    if cpuGuess == 'Rock!':
      tie()
    if cpuGuess == 'Paper!':
      loss()
      cpuScore += 1
    if cpuGuess == 'Scissors!':
      win()
      playerScore += 1
  elif guess == 'paper' or guess == 'p':
    print("I guessed " + cpuGuess)
    if cpuGuess == 'Rock!':
        win()
        playerScore += 1
    elif cpuGuess == 'Paper!':
        tie()
    elif cpuGuess == 'Scissors!':
        loss()
        cpuScore += 1
  elif guess == 'scissors' or guess == 's':
    print("I guessed " + cpuGuess)
    if cpuGuess == 'Rock!':
      loss()
      cpuScore += 1
    if cpuGuess == 'Paper!':
      win()
      playerScore += 1
    if cpuGuess == 'Scissors!':
      tie()
  else:
    print('invalid command!')
  if playerScore == 5:
    print('You Win!')
    break
  if cpuScore == 5:
    print('You Lose!')
    break