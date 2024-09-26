"""
@bastien.rossiaud
bastien.rossiaud@cpe.fr
26/09/2024
to do : tout le main code
"""

import functions_TP2 as f


phrase = f.saisir_entree() #initialisation de la phrase à valider

if f.verif_entree(phrase) == True :     #vérification de la présence des mots dans le dictionnaire
    liste = f.transformation(phrase)    #si phrase vérifiée transformation des mots de la phrase en valeur

etat=f.etats[0] #initialisation du premier état

for i in range(len(liste)) :    #programme de vérification de la validité de la phrase
    etat_act = f.table_de_transitions[etat,liste[0]]
    f.action_selon_sortie(etat_act,liste,i)