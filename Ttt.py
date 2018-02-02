from __future__ import print_function
#I have created this function to use later on in my code
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



ttt()
