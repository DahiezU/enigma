
# clé principale : a = 3, b = 4 , u0 = 7

# clé principale : a = 2, b = 5 , u0 = 6
# tab ::: [6, 17, 13, 5, 15, 9, 23, 25, 3, 11, 1, 7, 19, 17, 13]

tab = []
def creationCleSecondaire (a, b, u, modulo):
    
    if(len(tab) < 15):
        if(len(tab) == 0):
            tab.append(u)
        tab.append((a*u+b) % modulo)
        creationCleSecondaire(a, b, tab[len(tab) -1], modulo)
        


def desSimplifie(message, cle):
    tabMessage = []
    tabCle = []
    tailleBlock = 8
    for lettre in message:
        tabMessage.append(lettre)
    for lettre in cle:
        tabCle.append(lettre)
   
    print(tabMessage)
    partieGauche = tabMessage[0 : 4]
    partieDroite = tabMessage[4 : 8]
    print(partieDroite)

    for i in range (len(partieDroite)):
        if(i == 0):
            partieDroite.append(partieDroite[i])
            partieDroite.pop(0)
    print(partieDroite)

    for i in range (len(partieGauche)):
        
            partieGauche[i] = chr(ord(partieGauche[i])+ord(tabCle[i])) 

        



    messageInverse = partieDroite + partieGauche
    print(messageInverse)



desSimplifie("absdefgh", "ijkl")


        

