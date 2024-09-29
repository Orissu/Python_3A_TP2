"""
@bastien.rossiaud
bastien.rossiaud@cpe.fr
26/09/2024
to do : None
"""

import re as r #import d'une bibliothèque pour la méthode split 
                # elle va permettre de filtrer les caractères spéciaux

#définition de l'automate par son alphabet d'entrées, son alphabet de sortie et son ensemble d'état
#on rajoute à cela une table de transitions

#Types
entrees = (0,1,2,3,4,5)
etats = (0,1,2,3,4,5,6,7)
sorties = [8,9] #état 8 : erreur; état 9 : validation;

#Variable
table_de_transitions = [[1,8,8,8,4,8],
                        [8,1,2,8,8,8],
                        [8,2,8,3,8,8],
                        [5,8,8,8,7,9],
                        [8,8,8,3,8,8],
                        [8,5,6,8,8,8],
                        [8,6,8,8,8,9],
                        [8,8,8,8,8,9],
                        [8,8,8,8,8,8],
                        [9,9,9,9,9,9]]


#définition du dictionnaire de mots
dictionnaire = { "le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
                "mange" : 3, "petite" : 1, "joli" : 1, "grosse" : 1,
                "bleu" : 1, "verte" : 1, "dort" : 3, "julie" : 4, "jean" : 4, "." : 5}

def saisir_entree():
    """
    fonction qui permet de rentrer une phrase.
    in : None
    out : str
    """
    phrase = str(input("Veuillez rentrer une phrase avec les mots du dictionnaire : " ))
    return phrase

def transformation_str_lst(phrase) :
    """fonction qui transforme un string en lst de str
    in : str
    out : lst de str"""
    res = r.split(r'[^\w]+',phrase)    #permet de séparer par caractère spécial
    res.pop(-1)         #enlève l'élément vide du au re.split
    if phrase[-1] == '.' : 
        res.append('.')     #on rajoute le . s'il y en a un
    return res

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

def transformation_lst_int(liste):
    """
    fonction qui transforme une liste de str en une liste de valeur par rapport au dictionnaire de référence "dictionnaire"
    in : lst de str
    out : liste d'entiers correspondant aux entrées de l'alphabet d'entrée
    """
    liste_valeurs = []
    for element in liste : 
        liste_valeurs.append(dictionnaire[element])
    return liste_valeurs

def validite(etat_act):
    """
    fonction qui vérifie la validité de la phrase.
    in : etat_act un entier qui correspond à l'état actuel. 
    out : un booléen vérifiant la validité de la phrase """
    return etat_act == sorties[1]