"""
@bastien.rossiaud
bastien.rossiaud@cpe.fr
26/09/2024
to do : tout le coding des fonctions en dur (voir feuille pour algo)
"""


#définition de l'automate par son alphabet d'entrées, son alphabet de sortie et son ensemble d'état
#on rajoute à cela une table de transitions

#Types
entrees = (0,1,2,3,4,5)
etats = (0,1,2,3,4,5,6,7)
sorties = (8,9)

#Variable
table_de_transitions = [[1,8,8,8,4,8],
                        [8,1,2,8,8,8],
                        [8,2,8,3,8,8],
                        [5,8,8,8,7,9],
                        [8,8,8,3,8,8],
                        [8,5,6,8,8,8],
                        [8,6,8,8,8,9],
                        [8,8,8,8,8,9]]


#définition du dictionnaire de mots
dictionnaire = { "le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
                "mange" : 3, "petite" : 1, "joli" : 1, "grosse" : 1,
                "bleu" : 1, "verte" : 1, "dort" : 3, "julie" : 4, "jean" : 4, "." : 5}

def saisir_entree():
    """
    fonction qui permet de rentrer une phrase et la sépare par mot
    in : str (la phrase)
    out : lst de str
    """
    phrase = str(input("Veuillez rentrer une phrase avec les mots du dictionnaire suivant : ",dictionnaire))
    return phrase.split()

def verif_entree(phrase):
    """
    fonction qui vérifie si la chaine de caractere est bien composée de mots du dictionnaire
    in : une liste de mots composant une phrase
    out : Booléen
    """
    for mot in phrase :
        if mot not in dictionnaire.keys() : 
            return False
    return True

def transformation(liste):
    """
    fonction qui transforme une liste de str en une liste de valeur par rapport au dictionnaire de référence "dictionnaire"
    in : lst de str
    out : liste d'entiers correspondant aux entrées de l'alphabet d'entrée
    """
    liste_valeurs = []
    for element in liste : 
        liste_valeurs = liste_valeurs.append(dictionnaire[element])
    return liste_valeurs

def action_selon_sortie(etat_act,liste,i):
    """
    fonction qui transforme l'état actuel en l'état d'après selon les entrées. Elle suit le/la schéma/table de transition.
    in : etat_act un entier qui correspond à l'état actuel. liste est une liste contenant les mots de la phrase à vérifier transformées en valeurs.
    out : un booleen si on est à la fin de la phrase ou si la phrase est fausse. peut renvoyer un int etat_act pour passer à l'état suivant.
    """
    if etat_act == sorties[0] :
        print("Ceci n'est pas une phrase valide !")
        return False
    elif etat_act == sorties[1] : 
        print("Ceci est une phrase valide !")
        return True
    else : 
        etat_act = table_de_transitions[liste[i],liste[i+1]]
        return etat_act

