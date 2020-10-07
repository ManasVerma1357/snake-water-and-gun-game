''' 4.10.12
author-manas verma
snake, water, gun game
Now moving on to instructions.[ ignore, this is for me:| ]

You have to use a random choice function that we studied in tutorial #38, to
select between, snake, water, and gun.

You do not have to use a print statement in case of the above function.

Then you have to give input from your side.

After getting ten consecutive inputs, the computer will show the result based on each iteration.
You have to use loops(while loop is preferred).'''

import random

print('XXXXXXXXXXXXXSnake, Water, Gun gameXXXXXXXXXXXXXXXXXXXXX')


def wingame(you, comp):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return True
        elif you == 'g':
            return True,
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
i = 0
score = 0
while (i == 0):

    ra = random.randint(1, 3)
    if ra == 1:
        comp = 's'
    elif ra == 2:
        comp = 'w'
    elif ra == 3:
        comp = 'g'

    print('Computer Turn: Snake(s) Water(w) Gun(g)?')
    you = input('Your Turn: Snake(s) Water(w) Gun(g)?')
    print(f'Computer Chose {comp}')
    print(f'You Chose {you}')

    if wingame(you, comp) == None:
        print('Tie')

    elif wingame(you, comp):
        print('You Win!!')
        score = 5 + score
        print(score)

    else:
        print("You Lose!!\ngame over")
        i = int(input('Continue(0) Exit(1)?'))






















