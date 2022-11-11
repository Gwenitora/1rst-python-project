# Admettre que la fonction input(str) avec comme paramètre facultatif str permet à l'utilisateur de renvoyer un string en retour de l'execution de cette fonction, str permet d'afficher un message devant l'interaction du joueur
# Admettre que la fonction randint(x, y) avec comme paramètre x et y permet de renvoyerun entier naturel aléatoire compris entre x compris et y compris  en retour de l'execution de cette fonction

# Définir la fonction question avec comme paramètres un string nommé text et une liste nommé table et a comme valeur par défaut []
    # Définir length au retour de l'exection len avec comme paramètre table
    # Définir lengthStr au retour de l'execution de la fonction str avec comme paramètre (length - 1)
    # Si length est supérieur à 0
        # Alors:
        # Définir lengthList au retour de l'execution range avec comme paramètre length

    # Définir reponsePossible à "\nRéponse possible:\n"
    # Pour i commence à zero, s'incremente de 1 à chaque itération, et continue tant que i est inférieur à length
        # Alors:
        # Définir reponsePossible à la concaténation de reponsePossible, de '(', du retour de la fonction str avec comme paramètre i, de ") ", de l'élément en index i dans la list table, et de "\n"


    # Définir reponse au retour de l'execution de la fonction input avec comme paramètre la concaténation de text et de reponse possible
    # Essayer:
        # Définir reponse au retour de la fonction int avec comme paramètre reponse
        # Définir check à True
    # Sinon:
        # Définir reponse à ''

    # Si length est supérieur à 0
        # Alors:
        # Définir check à l'assertion ou reponse n'est pas dans lengthList
    
    # Tant que check
        # Alors:
        # Executer la fonction print avec comme paramètre la concaténation de "Erreur: Veuillez entrez une valeur entre 0 et " et de lengthStr
        # Définir reponse au retour de l'execution de la fonction input avec comme paramètre la concaténation de text et de reponse possible
        # Essayer:
            # Définir reponse au retour de la fonction int avec comme paramètre reponse
            # Définir check à True
        # Sinon:
            # Définir reponse à ''

        # Si length est supérieur à 0
            # Alors:
            # Définir check à l'assertion ou reponse n'est pas dans lengthList
    
    # Retourner reponse

# Définir la fonction play
