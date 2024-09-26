"""
@bastien.rossiaud
bastien.rossiaud@cpe.fr
26/09/2024
to do : faire du tri dans le main plus tout le document sur les tests
"""

import functions_TP2 as f


phrase = f.saisir_entree() #initialisation de la phrase à valider

if f.verif_entree(phrase) == True :     #vérification de la présence des mots dans le dictionnaire
    liste = f.transformation(phrase)    #si phrase vérifiée transformation des mots de la phrase en valeur



etat=f.etats[0] #initialisation du premier état

first_word = liste[0]

#parcourir les elements plutot que les indices
i=0
while i<len(liste)-1:    #programme de vérification de la validité de la phrase
    etat_act = f.table_de_transitions[etat][first_word]
    f.action_selon_sortie(etat_act,liste,i)
    i+=1


