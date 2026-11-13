#! /usr/bin/env python3

"""
Ce programme prendra sur son entrée standard les 6 cartons tirés au sort suivis du nombre à
trouver. Par exemple, si les cartons tirés sont 3 5 7 9 25 50 et que le nombre à découvrir est
859, il devra être appelé ainsi : echo 3 5 7 9 25 50 859  | ./compteestbon.py 
"""

from TAD.piles_listes_python import Pile
from TAD.files_listes_python import File
from notation_polonaise_inverse import eval_NPI_liste

def parcours_DFS(cartons, cible):

    pile = Pile()
    nb_noeuds = 0
    meilleure_expression = None
    

    for i, c in enumerate(cartons):
        restants = cartons[:i] + cartons[i+1:]
        pile.empiler(([c], restants))
        
    while not pile.est_vide():
        expr, restants = pile.depiler()
        nb_noeuds += 1
        
        valide, resultat = eval_NPI_liste(expr)
        
        if not valide:
            continue
            
        if resultat == cible:
            meilleure_expression = expr
            print(f"Solution trouvée (DFS) : {' '.join(str(x) for x in expr)} = {resultat}")
            break 

        if len(restants) > 0:
            for i, c in enumerate(restants):
                suivants = restants[:i] + restants[i+1:]
                for op in ['+', '-', '*', '/']:
                    pile.empiler((expr + [c, op], suivants))
                    
    return nb_noeuds, meilleure_expression


def parcours_DFS_recursif(choisis, restants, cible):

    nb_noeuds = [0]
    meilleure_solution = [None]

    def explorer(expr, restants_locaux):
        nb_noeuds[0] += 1
        valide, resultat = eval_NPI_liste(expr)
        
        if not valide:
            return False
            
        if resultat == cible:
            meilleure_solution[0] = expr
            print(f"Solution trouvée (DFS récursif) : {' '.join(str(x) for x in expr)} = {resultat}")
            return True
            
        if len(restants_locaux) == 0:
            return False
            
        for i, c in enumerate(restants_locaux):
            suivants = restants_locaux[:i] + restants_locaux[i+1:]
            for op in ['+', '-', '*', '/']:
                if explorer(expr + [c, op], suivants):
                    return True
        return False

    explorer(choisis, restants)
    return nb_noeuds[0], meilleure_solution[0]


def parcours_BFS(cartons, cible):
    "-BFS-"
    file = File()
    nb_noeuds = 0
    meilleure_expression = None
    
    for i, c in enumerate(cartons):
        restants = cartons[:i] + cartons[i+1:]
        file.enfiler(([c], restants))
        
    while not file.est_vide():
        expr, restants = file.defiler()
        nb_noeuds += 1
        
        valide, resultat = eval_NPI_liste(expr)
        
        if not valide:
            continue
            
        if resultat == cible:
            meilleure_expression = expr
            print(f"Solution trouvée (BFS) : {' '.join(str(x) for x in expr)} = {resultat}")
            break
            
        if len(restants) > 0:
            for i, c in enumerate(restants):
                suivants = restants[:i] + restants[i+1:]
                for op in ['+', '-', '*', '/']:
                    file.enfiler((expr + [c, op], suivants))
                    
    return nb_noeuds, meilleure_expression

    
