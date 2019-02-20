#!/usr/bin/env python3
from utils.input import nb_a, nb_c, A, Tab, afficher, Aa
import numpy as np
from termcolor import colored

A[np.triu_indices(nb_c, 1)[::-1]] = 1/A[np.triu_indices(nb_c, 1)]
afficher('la matrice de comparaison critere * critere', A)

# Somme des colonnes
S = A.sum(axis=0)
afficher('Somme des colonnes', S)

# la normalisation de la matrice de comparaison en divisant par la somme de chaque colonne

An = A / S
# l affichage de la matrice normalisee
afficher('la matrice de comparaison critere * critere normalisee ', An)

# calcul du vecteur propre
V = An.sum(axis=1)
Vp = V/nb_c
afficher('le vecteur propre', Vp)

# l affichage de la matrice normalisee
Avp = A*Vp
afficher('affichage de la matrice normalisee', Avp)

# Vecteur Poids
w = Avp.sum(axis=1)
afficher('le vecteur poids', w)


# calcul du vecteur ratio
Vr = w/Vp
afficher('le vecteur ratio', Vr)


# calcul de lamdamax
LamdaMax = Vr.sum()/nb_c
print(f'la valeure de lamdamax = {LamdaMax:.4f}')

# calcul de l indice de de coherence
Ci = (LamdaMax - nb_c) / (nb_c - 1)
print(f'l indice de coherence CI = {Ci:.4f}')

Ri = Tab[nb_c]
if Ri == 0.00:
    raise Exception('impossible Ri est 0')

print(f'l indice aleatoire RI = {Ri:.4f}')

# calcul du ratio de coherence
Cr = Ci / Ri
print(f'le ratio de coherence = {Cr:.4f}')

if Cr > 0.1:
    raise Exception(
        'la matrice de comparaison critere * critere est rejetee veuillez implementer une nouvelle matrice de comparaison')
else:
    print("la matrice de comparaison critere * critere est acceptee ")

print()

# La matrice de comparaison alternative * alternative pour chaque critere
for i in range(nb_c):
    Aa[i][np.triu_indices(nb_a, 1)[::-1]] = 1/Aa[i][np.triu_indices(nb_a, 1)]
    afficher(f'Matrice a*a pour le critere {i}', Aa[i])

    # Somme des colonnes
    s = Aa[i].sum(axis=0)
    Sa = np.append(Sa, [s], axis=0) if i else np.array([s])
    afficher(f'Somme des colonnes', Sa[i])

    # la normalisation de la matrice de comparaison en divisant par la somme de chaque colonne
    ana = Aa[i]/Sa[i]
    Ana = np.append(Ana, [ana], axis=0) if i else np.array([ana])
    afficher(f'normalisation de la matrice de comparaison', Ana[i])

    # Calcul du vecteur propre de chaque critere
    vpa = Ana[i].sum(axis=1)/nb_a
    Vpa = np.append(Vpa, [vpa], axis=0) if i else np.array([vpa])
    afficher(f'vecteur propre de chaque critere', Vpa[i])

# Matrice A * C
Mac = Vpa.transpose()
afficher(f'la matrice alternative * critere ', Mac)

R = (Mac * Vp).sum(axis=1)
afficher(f'la matrice R ', R)

position = (-R).argsort()
classement = position+1

print(colored(f'''
le classement des alternatives selon les criteres et les ponderations utilises:
{classement}
la meilleure solution est l\'alternative numero {classement[0]}''',
              'green'))
