myTable = [5,8,6,1,9,4,3,] #taille 7

buffer = 0

#Le tri a bulle est lent car il s'applique sur une grande partie du tableau qu'il a déja trié
#Ainsi pour chaque boucle il vas a nouveau reverifier chaque paire une a une et fera au minimum en nombre d'itération la grandeur du tableau-1
#de meme chaque verification sera au minimum fait (la grandeur du tableau -1)²
#J'ai dans cette version mis en affichage chaque fois que le tableau est verifié ou qu'une itération est finie ainsi que mis en avant a chaque fois qu'était fait une transmutation

for j in range(len(myTable)-1):
    for i in range(len(myTable)-1):

        if(myTable[i]>myTable[i+1]):    

            buffer = myTable[i]
            myTable[i]=myTable[i+1]
            myTable[i+1] = buffer
            print("Permutation !")

        print(myTable)
    print("le tableau au bout de ",j+1," itération vaut")
    print(myTable)


print("le tableau final vaut")
print(myTable)

#On voit ainsi que vers la fin de l'algorithme presque plus aucune permutation n'est éfféctué cependant l'algorithme verifie tout de meme
#Ainsi pour cette algorithme le temps de traitement du tableau est au carré de sa taille