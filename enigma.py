# Burdy Simon Ulysse Dahiez 
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
        


def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs



def desSimplifie(message, cle):
    tabMessage = []
    tabCle = []
    tailleBlock = 8


    for lettre in message:
        tabMessage.append(lettre)

    for lettre in cle:
        tabCle.append(lettre)

    partieGauche = tabMessage[0 : 4]
    partieDroite = tabMessage[4 : 8]
            

    for i in range (len(partieDroite)):
        if(i == 0):
            partieDroite.append(partieDroite[i])
            partieDroite.pop(0)
            

    for i in range (len(partieGauche)):
        partieGauche[i] = chr(     ord(partieGauche[i])    +   ord(tabCle[i])   ) 
        messageInverse = partieDroite + partieGauche
    
    maString = "".join(messageInverse)
    print(maString)

    return   maString
   




def desMessageLong(message, cle):
    tabMessage = []
    tabCle = []
    tailleBlock = 8
    tabDeMessages = []
    maGrosseString = ""

    res = []
    maGrosseString

    for lettre in message:
        tabMessage.append(lettre)

    for lettre in cle:
        tabCle.append(lettre)
    
    if(len(tabMessage) % 8 == 0):
        if(len(tabMessage) > 8):
            tabDeMessages = split(tabMessage,8)
            #print("tab des messages " , tabDeMessages)
            for elem in tabDeMessages:
                #print(elem)
                elemString = "".join(elem)
                res.append(desSimplifie(elemString,cle))
            
            
                
            for elem in res :
                maGrosseString += elem
            
            #print (maGrosseString)
            return maGrosseString

        else:
            desSimplifie(message,cle)

    
    else:  
        print("error")  






def desFinal(message, cle,nbRep):

    if(nbRep == 0):
        print(message)

    messageFinal = desMessageLong(message,cle)
    i = 0

    while (i != nbRep-1):
        messageFinal =  desMessageLong(messageFinal,cle)
        i += 1

    print(messageFinal)



#desSimplifie("aaaaaaaa" , "abcd")
#desFinal("aaaaaaaaaaaaaaaa","ijkl",8)

        

'''print(ord("Â") - ord("a"))
print(ord("Ã") - ord("b"))
print(ord("Ä") - ord("c"))
print(ord("Å") - ord("d"))


print(chr(97))'''