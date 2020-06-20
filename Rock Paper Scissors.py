import random

# GLOBAL VARIABLE
winner = None # Bot or Player
is_game_running = False # checks if the game is running or not
player_points = 0
bot_points = 0

# Run The Game
def play_game():
  global is_game_running
  is_game_running = True
  game()


# Check who is the winner (BOT or Player)
def game():
  global winner
  global is_game_running
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
    restart()   
  elif playerChoice == 'scissors' and botChoice == 'paper':
    print('')
    print('You WON!')
    winner = 'Player'
    restart()
  elif playerChoice == 'paper' and botChoice == 'rock':
    print('')
    print('You WON!')
    winner = 'Player'
    restart()
  # Bot Win Conditions
  elif botChoice == 'rock' and  playerChoice == 'scissors':
    print('')
    print('Bot WON, You Lose')
    winner = 'bot'
    restart()
  elif botChoice == 'scissors' and  playerChoice == 'paper':
    print('')
    print('Bot WON, You Lose')
    winner = 'bot'
    restart()
  elif botChoice == 'paper' and playerChoice == 'rock':
    print('')
    print('Bot WON, You Lose')
    winner = 'bot'
    restart()
  # Tie Conditions
  elif playerChoice == 'rock' and botChoice == 'rock':
    print('')
    print('Tie')
    winner = None
    restart()
  elif playerChoice == 'scissors' and botChoice == 'scissors':
    print('')
    print('Tie')
    winner = None
    restart()
  elif playerChoice == 'paper' and botChoice == 'paper':
    print('')
    print('Tie')
    winner = None
    restart()
    


# function that restarts for another round based on the user is input
def restart():
    is_restart = input("do you want to play another round? [y/n]: ")
    if is_restart == "y":
        play_game()
    else:
        is_game_running = False







play_game()
    



















# input(rock,paper,scissors)
# results
# who Win   
# bot Choice 
