
myTable = [5,8,6,1,9,4,3,] #taille 7

indicePermutaionA = 1
indicePermutaionB = 6

buffer = 0

print(myTable)

buffer = myTable[indicePermutaionA]
myTable[indicePermutaionA]=myTable[indicePermutaionB]
myTable[indicePermutaionB] = buffer

print(myTable)