import random
secret = random.randint(1,5)
guess = None
count = 0

while guess != secret:
  guess = input('I am thinking of a number, guess which: ')
  try:
    if guess.isdigit() :
      guess = int(guess)
  except:
    print("Invalid input, try again!")
      
  if guess == secret:
      print (str(guess) + " is the right number!")
      count += 1
  
  elif guess < secret:
      print(str(guess) + " is too low, guess again!")
      count += 1

  elif guess > secret:
      print(str(guess) +" is too high, guess again!")
      count += 1

 #else: 
    #print("Invalid input,")
print("You got it! It took you " + str(count) + " guess(es)!")