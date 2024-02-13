# tri une liste de tuples par ordre décroissant en fonction de la valeur d'un index donné
def tri_insertion_decroissant(lst, index):
    for i in range(1, len(lst)):
        cle = lst[i]
        j = i - 1
        while j >= 0 and lst[j][index] < cle[index]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = cle


def solution_sacados(objets, w):
    # tableau des ratios valeur/poids
    ratios = [(i, objets[i][1] / objets[i][0]) for i in range(len(objets))]
    # trier le tableau par ordre décroissant des ratios
    tri_insertion_decroissant(ratios, 1)
    
    gain_total = 0
    poids_total = 0
    
    for index, ratio in ratios:
        objet = objets[index]
        while objet[0] + poids_total <= w:
            gain_total += objet[1]
            poids_total += objet[0]
    
    # affiche les valeurs
    print("Gain :", gain_total, "€")
    print("Poids du sac :", poids_total, "kg")

objets = [(2, 6), (6, 21), (8, 13), (12, 16)]
poids_max = 45
solution_sacados(objets, poids_max)