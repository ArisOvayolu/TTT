#I have created this function to use later on in my code
#comment 9th feb
def ttt():

    #empty array is called choices
    choices = []

    for x in range (0, 9) :
        choices.append(str(x + 1))

    #this will come in heavilt towards end of code, if winner = true game ends, if playeroneturn = true, player turn switches
    playerOneTurn = True
    winner = False

#here i am creating the board
    def printBoard() :
        print( '\n -----')
        print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
        print( ' -----')
        print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
        print( ' -----')
        print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
        print( ' -----\n')

    while not winner :
        printBoard()
        if playerOneTurn :
            print( "Player 1:")
        else :
            print( "Player 2:")
        #try and except allows me to easily control where the player enters their x or o
        try:
            #choice is equal to where the player enters
            choice = int(input(">> "))
        except:
            #error message
            print("please enter a valid field")
            continue
        #if player enters x or 0 in filled space, error message appears
        if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
            print("illegal move, please enter within free space")
            continue

        if playerOneTurn :
            #player1 gets x
            choices[choice - 1] = 'X'
        else :
            #player2 gets O
            choices[choice - 1] = 'O'

        playerOneTurn = not playerOneTurn

        for x in range (0, 3) :
            y = x * 3
            if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
                winner = True
                printBoard()
            if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
                winner = True
                printBoard()

        #player wins if...
        if((choices[0] == choices[4] and choices[0] == choices[8]) or
           (choices[2] == choices[4] and choices[4] == choices[6])) :
            winner = True
            printBoard()
    #win statement
    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
    playagain()

def playagain():

    playagain = raw_input("would you like to play again")

    if playagain == "y" or playagain == "yes":
        print("ok, thank you")
        ttt()
    elif playagain == "n" or playagain == "no":
        print("ok, thank you")
    else:
        print("please enter either yes or no")
        playagain()


ttt()
