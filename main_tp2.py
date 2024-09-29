"""
@bastien.rossiaud
bastien.rossiaud@cpe.fr
26/09/2024
to do : jeu de tests
"""

import functions_TP2 as f


#Jeu de tests
test = int(input("Quel test voulez vous effectuer ? (rentrez un nombre de 1 à 5) : "))
if test == 1 : 
    phrase = "le joli chat mange."
elif test == 2 : 
    phrase = "le ,joli chat; dort."
elif test == 3 : 
    phrase = "."
elif test == 4 : 
    phrase = "le joli chat joue."
else : 
    phrase = f.saisir_entree() #initialisation de la phrase à valider

phrase = f.transformation_str_lst(phrase)

if f.verif_entree(phrase) == False :     #vérification de la présence des mots dans le dictionnaire
    raise SyntaxError('La phrase ne fait pas partie du dictionnaire.')    #si phrase vérifiée transformation des mots de la phrase en valeur
liste = f.transformation_lst_int(phrase)

etat_act = f.etats[0] #initialisation du premier état

for element in liste :                      #on suit la table de transitions avec la phrase
    etat_act = f.table_de_transitions[etat_act][element]
verif = f.validite(etat_act)                #on vérifie à la fin si la phrase est bonne
print(verif)

