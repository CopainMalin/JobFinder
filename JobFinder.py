import numpy as np
import pandas as pd
import argparse

from src.tools import calcul_recommandation, calcul_conclusion

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Récupère le numéro du département.")
    parser.add_argument(
        "dep", metavar="dep", type=int, nargs="+", help="Le numéro du département"
    )

    dataset = pd.read_csv("data/bdd_finale.csv")

    dep = parser.parse_args().dep
    if dep not in dataset.DEP.unique():
        raise ValueError("Le departement specifie n'est pas dans la base de donnees.")

    nb_ent = (
        dataset.groupby(by="DEP").sum().loc[:, "Sum"].loc[dep]
        - dataset.groupby(by="DEP").sum().loc[:, "Micro"].loc[dep]
    ).values[0]
    nb_jobs = (dataset.groupby(by="DEP").mean().loc[:, "SNHM14"].loc[dep]).values[0]

    print(
        f"\n{nb_ent} entreprises dans votre departement pour un salaire median de {nb_jobs:.2f} eurps de l'heure.\n"
    )
    print(" L'analyse de notre robot JobFinder : ".center(100, "="))
    print("\n")
    message_emp, score_emp = calcul_recommandation(
        data=dataset.groupby(by="DEP").sum().loc[:, "Sum"]
        - dataset.groupby(by="DEP").sum().loc[:, "Micro"],
        x=(dataset.groupby(by="DEP").sum().loc[:, "Sum"].loc[dep]).values[0]
        - (dataset.groupby(by="DEP").sum().loc[:, "Micro"].loc[dep]).values[0],
        msg={
            0: "C'est un departement avec (tres) peu d'emplois.",
            1: "Il n'y a pas beaucoup d'emplois dans ce département.",
            2: "Le nombre d'emploi ne devrait pas etre un problème dans votre departement.",
            3: "Il y'a un tres grand nombre d'emplois disponibles dans votre departement, vous avez l'embarras du choix !",
        },
    )
    print(f"- Au niveau du nombre d'emplois : {message_emp}")
    message_rem, score_rem = calcul_recommandation(
        data=dataset.groupby(by="DEP").sum().loc[:, "SNHM14"].loc[dep],
        x=dep,
        msg={
            0: "Comptez vos deniers, ils pourraient être les derniers.",
            1: "Votre région n'est pas dans le haut du classement niveau salaire.",
            2: "Le salaire est satisfaisant dans votre departement.",
            3: "Cresus n'a qu'a bien se tenir, vous etes dans un departement riche !",
        },
    )
    print(f"- Au niveau de la remuneration : {message_rem}")
    print(f"- Au global : {calcul_conclusion(score_emp + score_rem)}")
    print(f"\n\n")
