### DEBUT

# Admettre que la fonction input(str) avec comme paramètre facultatif str permet à l'utilisateur de renvoyer un string en retour de l'execution de cette fonction, str permet d'afficher un message devant l'interaction du Joueur
# Admettre que la fonction randint(x, y) avec comme paramètre x et y permet de renvoyer un entier naturel aléatoire entre x compris et y compris en retour de l'execution de cette fonction
# Admettre que la fonction cls() sans paramètre qui va effacer la console
# Admettre que la fonction sleep(s) avec comme paramètre un nombre relatif nommé s, la fonction permet d'attendre s secondes avant de continuer l'execution

# Définir la fonction question avec comme paramètres un string nommé text et une liste nommé table et a comme valeur par défaut []
    # Executer la fonction cls

    # Définir length au retour de l'exection len avec comme paramètre table
    # Définir lengthStr au retour de l'execution de la fonction str avec comme paramètre (length - 1)
    # Si length est supérieur à 0
        # Alors:
        # Définir lengthList au retour de l'execution range avec comme paramètre length

    # Définir reponsePossible à "\nRéponse possible:\n"
    # Pour i commence à zero, s'incremente de 1 à chaque itération, et continue tant que i est inférieur à length
        # Alors:
        # Définir reponsePossible à la concaténation de reponsePossible, de '(', du retour de la fonction str avec comme paramètre i, de ") ", de l'élément en index i dans la liste table, et de "\n"

    # Définir reponse au retour de l'execution de la fonction input avec comme paramètre la concaténation de text et de reponsePossible
    # Essayer:
        # Définir reponse au retour de la fonction int avec comme paramètre reponse
        # Définir check à Vrai
    # Sinon:
        # Définir reponse à ''

    # Si length est supérieur à 0
        # Alors:
        # Définir check à l'assertion ou reponse n'est pas dans lengthList
    
    # Tant que l'assertion check est Vrai
        # Alors:
        # Executer la fonction cls

        # Executer la fonction print avec comme paramètre la concaténation de "Erreur: Veuillez entrez une valeur entre 0 et " et de lengthStr
        # Définir reponse au retour de l'execution de la fonction input avec comme paramètre la concaténation de text et de reponsePossible
        # Essayer:
            # Définir reponse au retour de la fonction int avec comme paramètre reponse
            # Définir check à Vrai
        # Sinon:
            # Définir reponse à ''

        # Si length est supérieur à 0
            # Alors:
            # Définir check à l'assertion ou reponse n'est pas dans lengthList
    
    # Executer la fonction cls
    # Retourner reponseJoueur

# Définir la fonction play
    # Définir chifumi à ["Pierre", "Feuille", "Ciseaux"]

    # Définir pointsPlayerUn à 0
    # Définir pointsPlayerDeux à 0

    # Définir playWithABot au retour de l'execution de la fonction question avec comme paramètre "Voulez vous jouer avec un bot ?" et ["Non", "Oui"]
    # Définir playerDeuxName à "Joueur 2"
    # Si playWithABot est égal à 1
        # Alors:
        # Définir playerDeuxName à "Bot"

    # Définir pointsMax au retour de l'execution de la fonction question avec comme paramètre "Combien faut-il de points pour gagné ?"

    # Tant que pointsPlayerUn n'est pas égal à pointsMax et que pointsPlayerDeux n'est pas égal à pointsMax
        # Alors:
        # Si playWithABot est égal à 0
            # Alors:
            # Définir playerUnHasPlay au retour de l'execution de la fonction question avec comme paramètre "Joueur 1, vous pouvez jouer à l'abris de regard !" et chifumi
            # Définir playerDeuxHasPlay au retour de l'execution de la fonction question avec comme paramètre "Joueur 2, vous pouvez jouer à l'abris de regard !" et chifumi
        # Sinon:
            # Définir playerUnHasPlay au retour de l'execution de la fonction question avec comme paramètre "Joueur 1, vous pouvez jouer !" et chifumi
            # Definir playerDeuxHasPlay au retour de l'execution de la fonction randint avec comme paramètre 0 et 2

        # Executer la fonction print avec comme paramètre la concaténation de "Joueur 1 à jouer " et de l'élément en index playerUnHasPlay dans la liste chifumi
        # Executer la fonction print avec comme paramètre la concaténation de playerDeuxName, de " à jouer ", de l'élément en index playerDeuxHasPlay dans la liste chifumi, et de "\n"

        # Si la formule ((playerUnHasPlay - 1) % 3) est égal à playerDeuxHasPlay
            # Alors:
            # Executer la fonction print avec comme paramètre "Joueur 1 gagne donc ce round"
            # Incrémenter pointsPlayerUn à 1
        # Sinon si la formule ((playerDeuxHasPlay - 1) % 3) est égal à playerUnHasPlay
            # Alors:
            # Executer la fonction print avec comme paramètre la concaténation de playerDeuxName, et de " gagne donc ce round"
            # Incrémenter pointsPlayerDeux à 1
        # Sinon:
            # Executer la fonction print avec comme paramètre "On dirais bien que ce tour-ci, personne ne gagne"

        # Executer la fonction print avec comme paramètre la concaténation de "\nLe Joueur 1 resort donc avec ", du retour de l'execution de la fonction str avec comme paramètre pointsPlayerUn, et de " points"
        # Executer la fonction print avec comme paramètre la concaténation de "Et le ", de playerDeuxName, de " avec ", du retour de l'execution de la fonction str avec comme paramètre pointsPlayerDeux, et de " points"
        
        # Executer la fonction sleep avec comme paramètre 3
    
    # Si pointsPlayerUn est égal à pointsMax
        # Alors:
        # Executer la fonction print avec comme paramètre "Joueur 1 est désormais proclamer grand gagnant de cette partie de chifumi"
    # Sinon:
        # Executer la fonction print avec comme paramètre la concaténation de playerDeuxName, et de " est désormais proclamer grand gagnant de cette partie de chifumi"
    
    # Executer la fonction sleep avec comme paramètre 3
    # Définir playAgain au retour de l'execution de la fonction question avec comme paramètre "Voulez vous rejouer ?" et ["Non", "Oui"]

    # Si playAgain est égal à 1
        # Alors:
        # Executer la fonction play
    # Sinon:
        # Executer la fonction print avec comme paramètre "Très bien, à bientôt\n"

### FIN