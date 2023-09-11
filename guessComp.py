import random 

def guess(x):
  random_number = random.randint(1,x)
  guess = 0 
  while guess != random_number :
    guess = int(input(f'Enter the number from 1 to {x}: '))
    if guess < random_number:
      print ('Sorry the guess number is too low ')
    elif guess > random_number :
      print ('Sorry the guess number is too high ')
  print (f'Congrats you have the guessed the correct number {random_number }')  

guess(10)
  
