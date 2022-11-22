
ligne1= [" ","X"," "]
ligne2= [" "," "," "]
ligne3= [" "," ","O"]
plateau = [ligne1,ligne2,ligne3]
separationLigneHorizontal= "-------"
currentString = ""


for compteurLigne in range(len(plateau)):
    
    for i in range (len(plateau[compteurLigne])):

        currentString = currentString + "|" +plateau[compteurLigne][i]
    
    currentString = currentString + "|"
    print(currentString)
    print(separationLigneHorizontal)
    currentString = ""
