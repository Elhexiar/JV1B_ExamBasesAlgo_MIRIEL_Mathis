
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


#Mon code de l'exercice 4 permet deja de jouer de maniere complete au tic tac toe ayant implemente chaque exercice a la suite
#Le voici cependant un peu plus commente

#Boucle principale avec condition de victoire
while(playingCondition == True):


    #Changement de joueur en fonction du tour
    if(turn%2 == 0):
        selectedPlayer = "X"
    else :
        selectedPlayer = "O"

    #Input du joueur sur le numpad
    while(correctinput == False):
        print("Select an input on the numpad")
        SelectedLine = 0
        selectedPosition = int(input())

        #ajustement de l'input du joueur dans des coordonnees comprehensible par mon programme et verification que le joueur n'est pas mis un chiffre invalide ou une position invalide
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

        #Verification si la position est libre
        if(correctinput == True):
            if(plateau[selectedLine][selectedPosition] != " "):
                correctinput = False
                print("Il y a deja quelque chose a cet endroit")

    

    correctinput = False
    
    #On applique l'input du joueur verifie a nos tableau
    plateau[selectedLine][selectedPosition] = selectedPlayer
    #On avance de 1 le tour ayant ete effectue ce qui nous permet de commencer au tour 1 et non 0 dès le debut des calcule et pour le reste des iterations
    turn = turn+1


    #On affiche le plateau
    for compteurLigne in range(len(plateau)):
            
        for i in range (len(plateau[compteurLigne])):

            currentString = currentString + "|" +plateau[compteurLigne][i]
            
        currentString = currentString + "|"
        print(currentString)
        print(separationLigneHorizontal)
        currentString = ""

    
    #verification des condition de victoire
    score = 0
    #On fait une verification pour chaque joueur
    for player in range(1):
        if(player%2 == 0):
            selectedPlayer = "X"
        else :
            selectedPlayer = "O"


        #verification horizontale
        for ligne in range(len(plateau)):
            for colonne in range(len(plateau[ligne])):
                if(plateau[ligne][colonne] == selectedPlayer):
                    score = score+1
            
            if(score ==  len(plateau)):
                playingCondition = False
                victor = selectedPlayer
            score = 0

        #verification horizontale
        for colonne in range(len(plateau)):
            
            for ligne in range(len(plateau[ligne])):

                if(plateau[ligne][colonne] == selectedPlayer):
                    score = score+1

            if(score ==  len(plateau)):
                playingCondition = False
                victor = selectedPlayer
            score = 0

        #verification diagonale
        #on verifie deja si celui du milieux est fait
        if(plateau[1][1] == selectedPlayer):
            if(plateau[0][0] == selectedPlayer and plateau[2][2] == selectedPlayer):
                playingCondition = False
                victor = selectedPlayer
            elif(plateau[2][0] == selectedPlayer and plateau[0][2] == selectedPlayer):
                playingCondition = False
                victor = selectedPlayer

    #dernier tour possible
    if(turn == 9 and playingCondition == True):
        playingCondition = False
        victor = "nobody"



print("victory to ", victor)

#Afin de transformer ce tic tac toe en puissance 4 il faudrait augmenter la taille des tableau (les for etant adapte a la taille des tableau il ne devrait pas y avoir besoin de les changer) pour correspondre 
#mais aussi ajouter dans la phase de verification le fait que la case sur laquel le joueur veux jouer doit etre occupe ou que ca soit la premiere ligne
#il faut aussi augmenter le score de verification a 4 et trouver une meilleur maniere de verifier les diagonales plus adapte
        


