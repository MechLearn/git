import random


x = random.randint(1,10)

max_try = 10
print (x)

while True:

 for intento in range (1, max_try + 1):
    num = int(input(f'Attempt {intento}: Enter a number from 1 to 10: '))

    if num > 10 :
        print("That option not is valid, please choose other number: ")
    elif num == -1:
         print("Oh man, you use cheat codes, well..., the number is: " + str(x)  ) 
    elif num == x and intento == 1:
           print('Congrulations!, You found the number in the first try! ')
           answer = input('You want reset the game? (Y/N) ')
           if answer.lower() != 'y':
               break
    elif num == x :
           print('Congrulations!, You found the number! ')
           answer = input('You want reset the game? (Y/N) ')
           if answer.lower() != 'y':
               break
    elif num > x : 
           print('The number that you select is upper')
           print("Attempts remaining: " + str(intento))
    elif num < x :
          print('The number that you select is lower')
          print("Attempts remaining: " + str(intento))
    else:
          print('The number not is the same, please try again!')
          print("Attempts remaining: " + str(intento))
 if intento == 10:
       answer = input('You want reset the game? (Y/N) ')
       if answer.lower() != 'y':
        break





     