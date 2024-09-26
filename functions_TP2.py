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

#Variables
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
    pass

def action_selon_sortie():
    pass

def init():
    pass

