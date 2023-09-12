import random 

def play():
  user = input("What is your choice ? 'r' for rock 'p' for paper and 's' for scissors:  ")
  computer = random.choice (['r','p','s'])

  if user == computer :
    return 'Draw'

  if if_win(user , computer):
    return 'You Win'
  return 'You Lost'  

def if_win(player , opponent ):
   # r>s p>r s>p
  if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent =='p'):
    return True

print(play())
