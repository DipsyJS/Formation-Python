# codig:utf-8

"""
Modules -> modularité (une des dernières parties)

"""
import math
# -----------------------------------------------------------------------------

"""
Envoyer un message dans la console au démarrage du programme
"""
print("Le code est démarré")


"""
Nommer une variable : Doit commencer par une lettre
                      Ne doit pas contenir de caractères spéciaux
                      Ne doit pas contenir d'espaces
                      Utiliser des underscores (_)

Exemples de variables utilisables : AgePersonne
                                    age_personne

Types standarts : Nombre entier numérique (int)
                  Nombre flottant (nombre à virgule, float)
                  Chaîne de caractère (Un mot / Phrase, str)
                  Booléen (bool)
                  Structure de connées qui contient une série de valeurs (listes)


    Autres : (dictionnaires, tuples, etc...)
Ces quatres types sont ceux que vous retrouverez le plus souvent.

Si un nombre est dans une chaîne de caractère (""), il ne pourra pas être lié
dans un calcul, car Python comprend que c'est un str, (une chaîne de caractère).
Une chaîne de caractère ne peux pas subir une opération.

La variable "agePersonneInt" ci dessous est un "int", donc un nombre entier.
La variable "agePersonneStr" ci dessous est un "str", donc une chaîne de caractères.
La variable "agePersonneFloat" ci dessous est un "float", donc un nombre à virgule.
La variable "agePersonneBool" ci dessous est un "bool", donc soit oui, soit non.
Vous remarquerez qu'on met une majuscule à False et à True sur les booléens*
en Python.

"""

agePersonneInt = 14
agePersonneStr = "15"
agePersonneFloat = "15.5"
agePersonneBool = False
agePersonneListes = ["15", "16", agePersonneInt, agePersonneStr]
"""

Astuce : Pour savoir le type de votre variable, "type" est là pour vous. Il se
présente comme ça -> type(nomvariable)
Utilisez le dans des print(), pour voir le résultat dans votre console quand vous
démarrez le programme.

Dans console, nous avons ce résultat :
<class 'int'>
<class 'str'>
<class 'str'>
<class 'bool'>
<class 'list'>

Il y a marqué "class" parce que le Python est totalement Objet. On y reviendra
plus tard.
"""
print(type(agePersonneInt))
print(type(agePersonneStr))
print(type(agePersonneFloat))
print(type(agePersonneBool))
print(type(agePersonneListes))

"""

Pour afficher une valeur comprise dans une variable dans votre console,
il faut faire : print(variable).

Si vous laissez dans votre print() les doubles apostrophes des chaînes de
caractères et que vous voulez afficher uen variable, cela affichera ce que
vous avez mis dans les doubles apostrophes.
"""


print(agePersonneInt)
print("agePersonneInt")

"""

Astuce : Si vous voulez afficher une valeur d'une variable et une chaîne de
caractères non déclarée dans une variable, vous pouvez faire ça :
print(agePersonneInt, " : Age de la personne")

Cette ligne affichera d'abord l'age mis dans la variable, puis le texte
que vous avez mis à côté.

On appelle ça concaténer.
"""
print(agePersonneInt, " : Age de la personne")

"""
Vous n'êtes pas contraint à une seule chose comme ça dans votre print,
Vous pouvez le faire autant de fois que vous voulez dans votre print,
il faut juste que ça soit relié par une virgule. Sans cette virgule, la
coloration syntaxique de votre éditeur de code vous le fera savoir, ou
si vous n'avez pas de coloration syntaxique, vous aurez une erreur au
lancement du programme.
"""

prix = 15.99
texte = "L'age de la personne est {} et le prix HT est de {} euros. C'est {} cher. "

print(texte.format(agePersonneInt, prix, "pas très"))


"""

Les accolades que nous avons mis dans la variable texte, on va dire que c'est des
petites boites, qui ne contiennent rien pour l'instant, mais qu'on va leur faire
contenir quelque chose.

Dans le print() que nous avons fait au dessus :

On dit à Python d'afficher le contenu de la variable texte, puis on va utiliser
sur texte une méthode qui s'appelle format. La méthode format va prendre en
paramètre dans l'ordre, les accolades que nous avons mis dans la variable texte.
Les variables que nous mettons dans les parenthèses de la méthode format seront
prises dans l'ordre par la console, puis les affichera. Nous pouvons évidement
concaténer, comme nous l'avons vu au dessus dans les print().

Nous pouvons utiliser des chaînes de caractères dans la méthode format. Cependant,
attention à ne pas trop surcharger cette méthode, pour bien pouvoir relire votre
code en cas d'erreur.


Nous pouvons aussi ne pas utiliser la variable texte, et mettre directement le
texte de celle ci dans une chaîne de caractères, puis faire .format
"""


print("L'age de la personne est {} et le prix HT est de {} euros. C'est {} cher. ".format(
    agePersonneInt, prix, "pas très"))


"""
C'est évidement moins lisible, mais une autre façon de faire si vous avez des
petites valeurs à afficher dans votre console.
"""


"""
-------------------------------------------------------------------------------

"""


"""
Nouvelle notion : Faire saisir des informations à un utilisateur dans la console.

Pour ceci, nous allons utiliser une autre méthode qui s'appelle "input()".
Vous devez l'utiliser dans une variable.
Votre input doit contenir un texte à transmettre à votre utilisateur. Par exemple :

Attention ! Input va lire ce que vous mettez dans les parenthèses comme une chaîne
de caractères, (str).


nomJoueur = input("Choisissez un nom de joueur pour pouvoir jouer : ")
print("Bienvenue", nomJoueur)
"""

nomJoueur = input("Choisissez un nom de joueur pour pouvoir jouer : ")

print("Bienvenue", nomJoueur)


"""

Rappel : Fonctions vues : print() -> afficher à l'écran
         input() -> entrer des informations au clavier
         type() -> donne le type d'une donnée, variable, etc...
         str.format() -> formater une chaîne de caractères
         int(), float(), str(), bool() -> "caster" une donnée, la convertir.

Rappel : str -> Chaîne de caractères
"""


"""
Nouvelle notion : Transformation.

Transformer, c'est caster une donnée, la convertir. Si je veux convertir une
chaîne de caractères en une chaîne de caractère, je vais faire :

joueurTest = 40
print(listes(joueurTest))
"""
joueurTest = 40
print(joueurTest)
print(str(joueurTest))


print("Notion : Opérateurs, faire des opérations en PYTHON.")
"""
Nouvelle grosse notion : Faire des opérations

Opérateurs : + (addition)
             - (soustraction)
             * (multiplication)
             / (division)
             % (modulo) -> reste d'une division Euclidienne

Attention, les multiplications, divisions sont prioritaires (comme en maths)
Mais aussi le modulo. (%).

Opérateurs d'affectations : 

variable = variable + X
variable += X

variable = variable - X
variable -= X

variable = variable * X
variable *= X

Si vous mettez des parenthèses à quelque chose qui n'est pas prioritaire, il
le deviendra automatiquement.

calcul3 = (5+3) * 7
print(calcul3)
"""

calcul3 = (5 + 3) * 7
print("Résultat opération avec des parenthèses prioritaires : ", calcul3)

calcul = 5 / 2
calcul2 = 5 % 2
calcul2 = float(calcul2)
calcul = float(calcul)

print("Résultat = ", calcul, "\nReste = ", calcul2)


"""
Astuce : Retour à la ligne

Pour revenir à la ligne, vous pouvez utilisez "\n".
"""


"""
Pour compléter et terminer cette partie : La modification de valeurs

Je prend pour exemple le niveau d'un personnage dans un jeu : 


Cette méthode n'est pas la bonne -> 
niveauPersonnage = input("Niveau de départ ? ")
niveauPersonnage = int(niveauPersonnage)
print("Niveau du personnage", niveauPersonnage)
print("Bravo, tu as gagné ! Tu gagnes un niveau")
niveauPersonnage = 3
print("Niveau du personnage", niveauPersonnage)

Cette méthode est la bonne -> 
niveauPersonnage = input("Niveau de départ ? ")
niveauPersonnage = int(niveauPersonnage)
print("Niveau du personnage", niveauPersonnage)
print("Bravo, tu as gagné ! Tu gagnes un niveau")
niveauPersonnage = niveauPersonnage + 1
print("Niveau du personnage", niveauPersonnage)
"""
niveauPersonnage = input("Niveau de départ ? ")
niveauPersonnage = int(niveauPersonnage)
print("Niveau du personnage", niveauPersonnage)
print("Bravo, tu as gagné ! Tu gagnes un niveau")
niveauPersonnage += 1
print("Niveau du personnage", niveauPersonnage)


"""
Nouvelle notion : Les conditions

identifiant = "Jonathan"
mdp = "passsecurise"

print("Interface de connexion : ")
user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")

print("Vous êtes connecté, bienvenue sur votre session", user_id)

Vérification : 

if user_password == mot_de_passe:
    print("Vous êtes connecté, bienvenue", user_id)
print("Je ne suis plus dans le if")

"""

identifiant = "Jonathan"
mdp = "passecurise"

print("Interface de connexion : ")
user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")
if user_id == identifiant and user_password == mdp:
    print("Vous êtes connecté, bienvenue", user_id)

print("Information -> Je ne suis plus dans le if de la vérification du mot de passe et du nom d'utilisateur. ")


"""
Opérateur de comparaison : == (égal à)
                           != (différent de)
                           < (plus petit que)
                           > (plus grand que)
                           <= (plus petit ou égal à)
                           >= (plus grand ou égal à)

Mots clés des conditions : if / elif / else
if -> si
elif -> sinon si
else -> sinon

Conditions multiples : and (et)
                       or (ou)
                       in / not (dans / pas dans)
"""
lettre_hasard = input("Entrez une lettre : ")

if lettre_hasard in "aeiouy":
    print(lettre_hasard, " est une voyelle")
else:
    print(lettre_hasard, " n'est pas une voyelle")


age = 37

if age <= 18:
    print("Tu n'es pas majeur")
elif age == 50:
    print("Tu as 50 ans")
else:
    print("Tu es majeur")

print("Fin du if")


"""
Valeurs Booléenes
"""

jeu_charge = True  # A ne pas oublier ! True = Vrai (= 1)

# Attention à ne pas faire -> if jeu_charge == 1, car ça revient à faire ça.
if jeu_charge:
    print("Le jeu est en marche")
else:
    print("Je jeu a été quitté")


"""
Si j'ai des valeurs à tester sur des fonctions : 
"""

age1 = input("Quel âge as-tu ? ")
age1 = int(age1)

if age > 0 and age <= 100:
    print("L'age est validé")
else:
    print("L'age est incorrect")

# Ou une autre condition similaire ->

if 0 < age <= 100:
    print("L'age est validé, tu as", age1, " ans")
else:
    print("L'age est incorrect")


"""
Nouvelle notion -> Les boucles

Pour automatiser cette taches, nous allons faire une boucle -> 

Tache à automatiser -> 

print("Tache à automatiser")
print("Tache à automatiser")
print("Tache à automatiser")
print("Tache à automatiser")
print("Tache à automatiser")
print("Tache à automatiser")
print("Tache à automatiser")
print("Tache à automatiser")

Pour l'automatiser, nous allons utiliser l'opérateur "while"

while 0 < 5:
    print("Tache à automatiser")
    0 += 7
"""

compt = 0

while compt < 5:
    print("Tache à automatiser")
    compt += 1
print("Je suis sorti de la boucle...")


"""
Exemple Drole -> CMD
"""

cmd_lance = True
print("")

while cmd_lance:
    # Instructions en rapport avec le CMD
    choixMenu = input("> ")

    if choixMenu == "again":
        continue

    if choixMenu == "quit":
        cmd_lance = False
    elif choixMenu == "hello":
        print("salut")
    else:
        print("Commande introuvable")

"""
Si vous faites du C, ou du C++, vous savez peut être que si on fait des conditions, 
des boucles, on peut faire i++ pour dire qu'on augmente la valeur i de 1, ou alors
++i, qui est de la préincrémentation. 
En python, ça n'existe pas, on est obligé de faire -> 

i = i + 1
i += 1
"""

"""
Boucles : while / for
Mots-Clés : break (casse la boucle) / continue (revient au début de la boucle)
"""

sentence = "coucou"

for letter in sentence:
    # on créer une variable temporaire, ici letter
    print(letter)
    # Dans le terminal, ça s'affichera comme ça parce que for va prendre chaque
    # lettre et va les stocker dans la variable temporaire letter
# c
# o
# u
# c
# o
# u


"""
Nouvelle notion (appronfondie) : Les Fonctions

Définition Fonction -> Une fonction est une boite, qui prend en paramètre un
algorythme pour produire un résultat

Une fonction ne doit contenir une seule vérification, c'est mieux. 

Fonctions Vues depuis le début du cours : print(), input()
                                          type(), int(), float(), str(), bool()
"""

print("Bonjour à tous, voici les fonctions :) !")


def say_salut():
    print("Salut tout le monde :) !")


# Je ne suis plus dans la fonction
say_salut()
# Si il y a des paramètres à transmettre, il faudra les mettre dans les
# parenthèses.


def dire(nom_personne="Le BledArt", message_personne="Salut !"):
    print("{} : {}".format(nom_personne, message_personne))


dire("Jason", "Bonjour à tous")
dire("Tom", "Salut !")

# Dans la dernière fonction, j'ai mis ="" après chaque paramètre, c'est pour dire
# que je ne mets rien dans l'appel , alors ça renverra ce qu'il y a dans ="".
# Attention à ne pas mettre ça dans l'appel de la fonction tout en bas. (dire("Tom", "Salut !"))

"""
Nouvelle notion : La modularité


"""


# On va importer un module, "math"

"""
Importer un module : import <nom_module>
                     from <nom_module> import <nom_fonction>
                     from <nom_module> import *
"""


resultat = math.sqrt(100)
print(resultat)

sinus = math.sin(42)
print(sinus)

"""
Programmation orientée objet
"""


class Humain:
    """
    Classe des êtres humains
    """

    def __init__(self, c_prenom, c_age):  # Self cible l'objet lui même
        print("Création d'un Humain...")
        self.prenom = c_prenom
        self.age = c_age


print("Lancement du programme...")

humain1 = Humain("Jojo", 34)
print("Prénom de H1 {}".format(humain1.prenom))
print("Age de H1 {}".format(humain1.age))
