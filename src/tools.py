import numpy as np


def calcul_recommandation(data, x, msg):
    borne_inf = np.quantile(data, 0.25)
    borne_mid = np.quantile(data, 0.5)
    borne_top = np.quantile(data, 0.75)

    if x < borne_inf:
        return msg[0], 0
    if x > borne_inf and x < borne_mid:
        return msg[1], 1
    if x > borne_mid and x < borne_top:
        return msg[2], 2
    else:
        return msg[3], 3


def calcul_conclusion(score):
    if score <= 2:
        return "Un conseil mon vieux, fuyez de la."
    elif score <= 4:
        return "C'est un departement correct, vous pouvez trouver votre bonheur."
    else:
        return "Votre departement est tres fertile à l'emploi, vous avez bien choisi mon brave."
