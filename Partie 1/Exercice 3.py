myTable = [5,8,6,1,9,4,3,] #taille 7

buffer = 0

for j in range(len(myTable)-1):
    for i in range(len(myTable)-1):

        if(myTable[i]>myTable[i+1]):    

            buffer = myTable[i]
            myTable[i]=myTable[i+1]
            myTable[i+1] = buffer


print("le tableau final vaut")
print(myTable)
