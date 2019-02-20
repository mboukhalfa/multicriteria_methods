import numpy as np
from termcolor import colored

np.set_printoptions(precision=4, suppress=True)

nb_a = 2
nb_c = 4

# implementation de la matrice de comparaison (critere x critere)
A = np.array([
    [1, 5, 9, 1],
    [0, 1, 3, 1/5],
    [0, 0, 1, 1/7],
    [0, 0, 0, 1]
])

# introduire le tableau RI
Tab = {
    1: 0.00,
    2: 0.00,
    3: 0.58,
    4: 0.90,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.41,
    9: 1.45,
    10: 1.49,
    11: 1.51,
}


def afficher(name, arr):
    print(colored(name, 'red'))
    print()
    print(arr)
    print()


def affiche(arr):
    print(arr)
    print()


# La matrice de comparaison alternative * alternative pour chaque critere
Aa = np.array([
    [[1, 5],
     [0, 1]],

    [[1, 1/3],
     [0, 1]],

    [[1, 1],
     [0, 1]],

    [[1, 7],
     [0, 1]]
])
