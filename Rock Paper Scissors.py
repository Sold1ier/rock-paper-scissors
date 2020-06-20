import random
# GLOBAL VARIABLE
winner = None # Bot or Player
gameRuning = False
# Run The Game
def playGame():
  global gameRuning
  gameRuning = True
  whoWin()
# Check who is the winner (BOT or Player)
def whoWin():
  global winner
  global gameRuning
  playerChoice = input('Choose rock paper or scissors: ')
  botChoice = ['rock', 'paper', 'scissors']
  botChoice = random.choice(botChoice)
  print('Your Choice: ' + playerChoice + ' ,Bot Choice: ' + botChoice)
  while playerChoice not in ['rock', 'paper', 'scissors']:
    print('')
    playerChoice = input('Input Error, Choose rock paper or scissors: ')
    print('Your Choice: ' + playerChoice + ' ,Bot Choice: ' + botChoice)
  # Player Win Conditions
  if playerChoice == 'rock' and botChoice == 'scissors':
    print('')
    print('You WON!')
    winner = 'Player' 
    gameRuning = False   
  elif playerChoice == 'scissors' and botChoice == 'paper':
    print('')
    print('You WON!')
    winner = 'Player'
    gameRuning = False
  elif playerChoice == 'paper' and botChoice == 'rock':
    print('')
    print('You WON!')
    winner = 'Player'
    gameRuning = False
  # Bot Win Conditions
  elif botChoice == 'rock' and  playerChoice == 'scissors':
    print('')
    print('Bot WON, You Lose')
    winner = 'bot'
    gameRuning = False
  elif botChoice == 'scissors' and  playerChoice == 'paper':
    print('')
    print('Bot WON, You Lose')
    winner = 'bot'
    gameRuning = False
  elif botChoice == 'paper' and playerChoice == 'rock':
    print('')
    print('Bot WON, You Lose')
    winner = 'bot'
    gameRuning = False
  # Tie Conditions
  elif playerChoice == 'rock' and botChoice == 'rock':
    print('')
    print('Tie')
    winner = None
    gameRuning = False
  elif playerChoice == 'scissors' and botChoice == 'scissors':
    print('')
    print('Tie')
    winner = None
    gameRuning = False
  elif playerChoice == 'paper' and botChoice == 'paper':
    print('')
    print('Tie')
    winner = None
    gameRuning = False
 
  







playGame()
    



















# input(rock,paper,scissors)
# results
# who Win   
# bot Choice 
