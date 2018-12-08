import sys
import os
import random
import collections
from colored import fg, bg, attr

# Definition of the colors
print ('%s Blue = 1 %s' % (fg(4), attr(0)))
print ('%s Green = 2 %s' % (fg(2), attr(0)))
print ('%s RED = 3 %s' % (fg(1), attr(0)))
print ('%s Yellow = 4 %s' % (fg(3), attr(0)))
print ('%s Orange = 5 %s' % (fg(58), attr(0)))
print ('%s Pink = 6 %s' % (fg(218), attr(0)))
print ('%s Purple = 7 %s' % (fg(54), attr(0)))
print ('%s White = 8 \n %s' % (fg(15), attr(0)))
print('''%s 		----------------- WARNING -----------------
	!!! ENTER ONLY INTEGERS AND NOT LETTERS OF THIS WON'T WORK !!! \n %s''' % (fg(1), attr(1)))

# Function used to play again or quit after a game
def play():
    global name
    answer = int(input("This answer is above. Do you want to play again ? Enter 1 for yes, 2 to quit, 3 with erase. \n"))
    if answer == 1:
        os.system('clear')
        menu()
    elif answer == 2:
        print("Game terminated. See you later", name, "!")
        print("%s Made with love by Félix and Duc-Thomas. %s" % (fg(1), attr(1)))
        sys.exit(0)
    elif answer == 3:
        os.system('clear')
        print("Game terminated. See you later", name, "!")
        print("%s Made with love by Félix and Duc-Thomas. %s" % (fg(1), attr(1)))
        sys.exit(0)

# Main body of the program
def main():
    global multi
    global name
    name = input("Enter your name : ")
    multi = int(input("Enter 1 for solo, 2 for multiplayer : "))
    while multi < 1 or multi > 2:
    	multi = int(input("Enter 1 for solo, 2 for multiplayer : "))
    access = int(input("Make a selection from the above list: "))
    while not access in [0, 1, 2, 3, 4, 5, 6, 7]:
    	access = int(input("Make a selection from the above list (between 0 & 7): "))
    os.system('clear')
    
    global ncolor
    global g
    global lst_mix_colors
    global lst_init_colors
    global lst_mix_colors_copy
    lst_init_colors = []
    lst_mix_colors = []
    lst_mix_colors_copy = []
    
    # Access to the menu
    if access == 0:
        menu()

    # Play in normal difficulty
    if access == 1:
        ncolor = 4
        g = 13
        print("Normal difficulty, you have 12 guesses and 4 colors. (1 to 4) \n")
        game()

    # Play in hard difficulty
    if access == 2:
        ncolor = 6
        g = 13
        print("Hard difficulty, you have 12 guesses and 6 colors. (1 to 6) \n")
        game()

    # Play in insane
    if access == 3:
        ncolor = 6
        g = 9
        print("Insane, you have 8 guesses and 6 colors. (1 to 6) \n")
        game()

    # Play in madness
    if access == 4:
        ncolor = 6
        g = 9
        print("Madness, you have 8 guesses and 8 colors. (1 to 8) \n")
        game()
            
    if access == 5:
        print("I guess you feel lucky ! Then good luck ! (4 colors). (1 to 4)  \n")
        for cpt3 in range (1, 5):
            if multi == 1:
                x = random.randint(1, 4)
                lst_init_colors.append(x)

                # Copy a list in another list
                lst_mix_colors = list(lst_init_colors)

                # Mix randomly the list
                random.shuffle(lst_mix_colors)

            if multi == 2:
                print("Enter the value number", cpt3, "of your list : ")
                x = int(input("Value = "))
                lst_mix_colors.append (x)

        print(lst_init_colors, 'initials colors')
        print(lst_mix_colors, 'mix colors')
        os.system('clear')
        print('Try to find the 4 correct colors, please enter your proposition :')
        integer = False
        while integer == False:
            try :
                testlist = []
                testlist = list(input("Enter your list of numbers : "))
                while len(testlist) != 4:
                    testlist = list(input("Enter a maximum of 4 values : "))
                for j in range(len(testlist)):
                    testlist[j] = int(testlist[j])
                    integer = True
            except :
                print("Retry with right values")
                integer = False
        print (testlist)
        if testlist == lst_mix_colors:
            print("Oh waw... You won ! Go play at the lottery today", name, "!")
        else:
            print("You loose. Not lucky enough...")

    # Play in free mode
    if access == 6:
        z = int(input("How many attempts do you want ? : \n"))
        while z <= 0:
        	z = int(input("How many attempts do you want ? (enter positive value) : \n"))
        g = z + 1
        ncolor = int(input('Choose a number of colors to play with : \n'))
        while ncolor <= 0:
            ncolor = int(input('Enter a positive value : '))
        game()
    
    if access == 7:
        print("""Pregame Setup
Decide who will be the code breaker and the code maker.

Both players position themselves at the ends of the game board.
The code maker should have the “secret code area” on their side of the board and should use the plastic cover to hide their secret code using the colored pegs.

Playing the Game
Once the code maker has created the secret code, the code breaker may place any combination of colored guess pegs on the first line of 4 (or more) peg holes.


The code maker will use the white pegs, which indicate each peg that is a correct color but wrong position, or a black peg to indicate each peg is in a correct position and a right color. If neither are true, then no peg should be placed. The code maker may place these pegs in any order in the peg holes arranged in the square pattern next to the line of peg holes holding the guess pegs being answered.

The answer and guess pegs stay in their positions until the end of the game.

Play continues until the code is discovered or there are no remaining guesses.

Players swap roles and play another round.

Winning the Game
The player that used fewer guesses to discover their opponent’s code wins. If neither player was able to discover their opponent’s code, then the game ends in a draw.""")    
    return play()

# !!! This is the menu !!!
def menu():
    print("%s Menu: \n %s" % (fg(1), attr(1)))
    print("%s     0. Menu %s" % (fg(15), attr(0)))
    print("     1. Normal difficulty : 12 guesses, 4 colors")
    print("     2. Hard difficulty : 12 guesses, 6 colors")
    print("     3. Insane : 8 guesses, 6 colors")
    print("     4. Madness : 8 guesses, 8 colors")
    print("     5. I feel lucky : 1 guess, 4 colors")
    print("     6. Feel free \n")
    print("     7. Rules")
    main()

def game():
    global name
    global ncolor
    global multi
    global g
    lst_mix_colors = []
    for cpt3 in range (1, 5):
        if multi == 1:
            x = random.randint(1, ncolor)
            lst_init_colors.append(x)

            # Copy a list in another list
            lst_mix_colors = list(lst_init_colors)

            # Mix randomly the list
            random.shuffle(lst_mix_colors)
        if multi == 2:
            print("Enter the value number", cpt3, "of your list : ")
            x = int(input("Value = "))
            while x <= 0:
            	x = int(input("Value = "))
            lst_mix_colors.append (x)
    print(lst_init_colors, 'initials colors')
    print(lst_mix_colors, 'mix colors')         
    os.system('clear')
    print('Try to find the 4 correct colors, please enter your proposition', name, ':')
    for cpt2 in range (1, g):
        integer = False
        while integer == False:
	        try :
	        	testlist = []
	        	testlist = list(input("Enter your list of numbers : "))
	        	while len(testlist) != 4:
	        		testlist = list(input("Enter a maximum of 4 values : "))
	        	for j in range(len(testlist)):
	           		testlist[j] = int(testlist[j])
	           		integer = True
        	except :
        		print("Retry with right values")
        		integer = False
        print (testlist)
        if testlist == lst_mix_colors :
            print("You won", name, "!")
            return play()
        # Control of the place good or not
        pepegs=0
        papegs=0
        lst_mix_colors_copy = []
                    
        for i in range(len(lst_mix_colors)):
            lst_mix_colors_copy.append(lst_mix_colors[i])
            e = lst_mix_colors[i]
            if testlist[i] == e:
                pepegs+=1 
                lst_mix_colors_copy.remove(testlist[i])
            elif testlist[i] in lst_mix_colors_copy :
                papegs+=1
                lst_mix_colors_copy.remove(testlist[i])
        print('¤HINTS¤ :\nPerfect pegs :', pepegs,'\nPartial pegs :', papegs,"\nCome on try harder", name, "!")

menu()