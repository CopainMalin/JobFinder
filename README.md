# JobFinder

Il vous faudra dans un premier lieu installer les 2 librairies python nécessaires (numpy et pandas, peuvent être installer sans passer par le requirements si les versions poses problème):
<br>
pip install -r requirements.txt
<br><br>

Pour exécuter l'application : <br>
launch.sh le_numero_de_votre_departement
<br><br>
Exemple :<br> 
launch.sh 75 -> La recommandation de JobFinder pour le département 75
<br><br>
Vous pouvez également passer directement par le script python :<br>
python JobFinder.py le_numero_de_votre_departement
<br><br>
Exemple :<br>
python JobFinder.py 75 -> La recommandation de JobFinder pour le département 75
<br><br>

/!\ Il peut être nécessaire de donner au préalable l'autorisation d'execution du script :<br>
chmod +x launch.sh
