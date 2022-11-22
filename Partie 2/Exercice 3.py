
ligne2= [" "," "," "]
ligne1= [" "," "," "]
ligne0= [" "," "," "]
plateau = [ligne2,ligne1,ligne0]
separationLigneHorizontal= "-------"
currentString = ""
selectedPlayer = "X"
correctinput =  False
turn = 0
playingCondition = True

while(playingCondition == True):


    if(turn%2 == 0):
        selectedPlayer = "X"
    else :
        selectedPlayer = "O"


    while(correctinput == False):
        print("Select an input on the keypad")
        SelectedLine = 0
        selectedPosition = int(input())

        if(selectedPosition<=3):
            selectedLine = 2
            selectedPosition = selectedPosition-1
            correctinput = True
        elif(selectedPosition<=6):
            selectedLine = 1
            selectedPosition = selectedPosition-4
            correctinput = True
        elif(selectedPosition<=9):
            selectedLine = 0
            selectedPosition = selectedPosition-7
            correctinput = True

        if(correctinput == True):
            if(plateau[selectedLine][selectedPosition] != " "):
                correctinput = False
                print("Il y a déja quelque chose a cet endroit")

    correctinput = False
    plateau[selectedLine][selectedPosition] = selectedPlayer
    turn = turn+1



    for compteurLigne in range(len(plateau)):
            
        for i in range (len(plateau[compteurLigne])):

            currentString = currentString + "|" +plateau[compteurLigne][i]
            
        currentString = currentString + "|"
        print(currentString)
        print(separationLigneHorizontal)
        currentString = ""

    score = 0
    #verification horizontale
    for player in range(1):
        if(player%2 == 0):
            selectedPlayer = "X"
        else :
            selectedPlayer = "O"

        for ligne in range(len(plateau)):
            for colonne in range(len(plateau[ligne])):
                if(plateau[ligne][colonne] == selectedPlayer):
                    score = score+1
            
            if(score ==  len(plateau)):
                playingCondition = False
                victor = selectedPlayer
            score = 0

print("victory to ", victor)


        


