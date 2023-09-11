
import random 

def computer_guess(x):
  low = 1 
  high = x 
  feedback = ''
  while feedback != 'c':
    if low != high :
      guess = random.randint(low , high)
    else :
      guess = low 
    feedback = input(f'Is {guess} is too high (H) , too low (l) or correct (c)').lower()
    if feedback == 'h':
      high = guess-1;
    elif feedback == 'l':
      low = guess + 1 
  print (f'Yay Congrats the number is {guess}')

computer_guess(10)
  
  
