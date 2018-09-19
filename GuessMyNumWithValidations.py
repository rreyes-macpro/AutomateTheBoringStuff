#Guess the number I am thinking in n tries
import random
rep = ' '
while rep != 'n':
  guesses = 0
  minnum = 1
  maxnum = 1000
  tries = 10
  #rep = ' '

#while rep != 'n':
  print("Hi there, welcome to my world")
  yourName = input("What is your name? ") #takes the name of the user who will be guessing the number
  
  mynum = random.randint(minnum,maxnum)
  
  print('Nice to meet you '+ yourName +' ,well I am thinking of a number from ' + str(minnum) +' to '+ str(maxnum) )

#####################################

  while guesses < tries:
    print('Guess my number in '+ str(tries - guesses)+' tries')
    print('Please type any number from '+ str(minnum) + ' to ' + str(maxnum))
    while True:
      try:
        guess = int(input())
      except ValueError:
        print("Please provide valid input, numbers only ! ")
        continue
      else:
        break
    #try:
    guess = int(guess)
    guesses = guesses + 1
    #except ValueError:
    #print('This is not a number!')
    
    #guesses = guesses + 1
    
    if (guess < minnum or guess > maxnum):
      print('Pay attention! I told you, the number is between '+ str(minnum) +' and '+ str(maxnum) +' only!')
  
    if guess < mynum:
      print('Your guess is too low. You only have '+ str(tries - guesses) +' tries left')
    
    if guess > mynum:
      print('Your guess is too high.You only have '+ str(tries - guesses) +' tries left')
    
    if guess == mynum:
      break
  ####################################

  if guess == mynum:
  #guesses = str(guesses)
    print('Good job ! How did you do that? You guessed my number which is ' + str(mynum) + ' in ' + str(guesses) + ' guesses!')
  
  if guess != mynum:
  #mynum = str(mynum)
    print('Sorry, not the right number.It was ' + str(mynum))
  
  rep = input("Type anything (except 'n') if you want to play again ")
print("Thanks for playing, have a nice day!")



