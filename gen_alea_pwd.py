# Elko RAMBELONOSOAVINA, le 02/07/2019 à Vitry-le-François
### Programme de génération de mot de passe aléatoire à l'aide d'un table de code ASCII

# Import des bibliothèques de fonctions utiles
import random

# Déclaration des variables
nchar = 0               # Nombre de caractères du mot de passe à générer
crypt_pwd = []          # Tableau de codes décimaux ASCII (entre 32 et 126) généré
decrypt_pwd = []        # Tableau de caractères équivaut aux codes ASCII du précédent variable
pwd = ''                # Le mot de passe généré aléatoirement par conversion
ans = 'G'               # Instruciton demandée par l'utilisateur
new_nchar = 'Y'         # Instruction pour renouveler le nombre de mot de passe
rand_int = 0            # Entier aléatoire entre 32 et 126 pour le code ASCII

# Informations à propos du programme pour l'utilisateur
print('This program generates randomly a password and you have to choice the number of characters in the password that you want ')

while ans != 'Q' and ans != 'q':
    # Vérification si l'utilisateur veut changer le nombre de caractères
    if new_nchar == 'Y' or new_nchar == 'y':
        nchar = 0
        # Demande du nombre de caractères désirés par l'utilisateur (min. 8 caractères)
        # Si option sans doublon, on peut considérer que le nombre max. de caractères ici sera de 95
        while nchar < 8 :
            nchar = int(input('Give the number of characters that you want (at least 8) : '))

    # Génération aléatoire du mot de passe et insertion dans un tableau [* OPTION SANS DOUBLON *]
    i = 0
    while i < nchar:
        if i == 0:
            crypt_pwd.append(random.randint(32,126))
            i = i+1
        else:
            rand_int  = random.randint(32,126)
            if rand_int != crypt_pwd[i-1] and i > 0:
                crypt_pwd.append(rand_int)
                i = i+1

    # Décryptage du mot de passe crypté en ASCII et génération du mot de passe en chaîne de caractères
    for j in range(0,nchar):
        decrypt_pwd.append(chr(crypt_pwd[j]))
        pwd = pwd + decrypt_pwd[j]

    # Affichage du mot de passe généré
    print(pwd)

    # Demande d'une nouvelle instruction
    ans = input('Something else ? : ')

    # Initialisation des variables si nouvelle instruction que "Quitter" le programme
    if ans == 'G' or ans == 'g':
        new_nchar = input('Would you want to change the number of characters? [Y/N] : ')
        crypt_pwd = []
        decrypt_pwd = []
        pwd = ''

# Test de la rédaction des mots de passe dans un fichier texte [* RUNNING *]
"""
text = open('test.txt','w')
text.write('This is the password generated randomly :\n')
text.write(pwd)
text.close()
"""
