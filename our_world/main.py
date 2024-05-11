import discord
import asyncio
from discord.ext import commands
import json
from dotenv import load_dotenv
import os
from typing import List
from rich.console import Console
from rich.table import Table
from rich.text import Text
import logging
import json
import logging
import os
import platform
import random
import sys
import datetime
from datetime import datetime, timedelta
import pytz
import aiosqlite
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv

import cours.PythonCog as PyC
import cours.JSCog as JSC
import cours.PHPCog as PHPC
import cours.HTMLCog as HTMLC
import cours.C_Cog as CC
import cours.CSSCog as CSSC
import cogs.TicketCog as TC

from database import DatabaseManager

excluded_cogs_list = ["b_Setup_bot.py"]

def get_json(fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        return json.load(f) 

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

class LoggingFormatter(logging.Formatter):
    # Colors
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)


logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())
# File handler
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or(config["prefix"]),
            intents=discord.Intents.all(),
            help_command=None,
        )
        """
        This creates custom bot variables so that we can access these variables in cogs more easily.

        For example, The config is available using the following code:
        - self.config # In this class
        - bot.config # In this file
        - self.bot.config # In cogs
        """
        self.logger = logger
        self.config = config
        self.database = None
        self.added_roles = []
        self.removed_roles = []

    async def PythonCours(self):
        # Récupération de la catégorie
        ch1_id = 1232425069184286740
        ch1 = self.get_channel(ch1_id)
        embed = discord.Embed(
            title="",
            description="# Variables\n## **C'est quoi une variable ?**\nNous allons voir aujourd'hui, les **variables**.\nPour commencer, une variable c'est comme une boîte où l'on stocke une information.\nCette information peut-être un texte appellé **chaine de caractère (string)**.\nOu, elle peut contenir un **nombre entier simple (integer)**.\n\n## **Variables en python**\nPour, en python, définir une variable, il faut qu'il n'y ai pas d'espace, ni de caractere speciaux sauf le underscore `_`.\nPar exemple, ici nous allons definir une variable prenom :\n```py\nprenom = \"GoldJust\"```\nNous mettons `GoldJust` entre guillemets entre \" car c'est une **chaine de caractère**.\nSi nous voulons afficher cette variable dans le terminal, nous allons utiliser la fonction `print()`\nPour utiliser une cette fonction, nous lui mettons en paramètre la variable ce qui donne :\n```py\nprenom = \"GoldJust\"\nprint(prenom)```\nSi nous voudrions définir un âge nous mettrons `age = 5`, le 5 **sans** guillemet car c'est un chiffre.\nSi, nous voulons par exemple afficher une phrase avec la variable age et la variable prenom, nous allons faire comme ceci :\n```py\nprenom = \"GoldJust\"\nage = 20\nprint(f\"Le membre {prenom} a {age} ans !\")```\nLe petit f sert a dire que ce qu'il y a entre les {} ce sera des variables.\nIl existe plusieurs manière de faire ça, notament avec des `+` ou encore des `,`.\nNous pouvons aussi changer la valeur d'une variable.\n```py\nprenom = \"GoldJust\"\nprint(prenom)\nprenom = \"Gold\"\nprint(prenom)```\nPython ecrira au debut `GoldJust` puis ensuite `Gold` car la valeur a changé.\n\n## **Input en python**\nVous pourrez avoir envie de demander son âge et son prénom à l'utilisateur.\nPour cela, nous allons utiliser la fonction `input()` qui permet de faire saisir à l'utilisateur quelque chose.\nVoici un exemple :\n```py\nprenom = input(\"Qu\'elle est votre prenom: \")\nage = input(\"Qu\'elle est votre age : \")\nage = int(age)\nage_suivant = age+1\nprint(f\"Bonjour {prenom}, l'année prochaine vous aurez {age_suivant} !\")```\nRemarquez qu'on utilise la fonction int à la ligne `3`, car l'input renvoie une chaine de caractère même si c'est un chiffre.\nPour le convertir en nombre, nous utilisons donc cette fonction.\nPuis, nous créons une nouvelle variable appelée `age_suivant` qui contient l'age saisi + 1.\nEnsuite, nous affichons le tout via un `print`.",
            color=discord.Color.blue()
        )
        view = PyC.Cours1Button()
        await ch1.purge()
        await ch1.send(embed=embed, view=view)


        ch2_id = 1232424986946572349
        ch2 = self.get_channel(ch2_id)
        embed = discord.Embed(
            title="",
            description="# Types de variables\n## String\nLe string est une chaine de caractère, en voici un exemple:\n```py\nchaine = \"Salut \"```\nIl est de type `str`.\nOn peut le voir via la fonction type :```py\nchaine = \"Salut \"\nprint(type(chaine))```\n\n\nOn peut utiliser la fonction str pour convertir un nombre en chaine :```py\nnombre = 5\nchaine = str(nombre)\nprint(type(nombre))\nprint(type(chaine))\n```\n\n## Integer\nUn `integer` est un chiffre entier.\n```py\nmon_nombre = 5\nprint(type(mon_nombre))\n```\nCa donnera en type `int`.\nPour convertir une chaine de caractère en nombre on peut utiliser la fonction int.\n**Attention** : La chaine doit être un chiffre entre \".```py\nchaine = \"5\"\nnombre = int(chaine)\nprint(type(chaine))\nprint(type(nombre))```\n\nCette fonction peut être utile pour les additions / soustractions.\n## Float\nUn `float` est un nombre à virgule.\nPour symboliser cette virgule nous utilisons le point :\n```py\nnombre_virgule = 5.5\nprint(type(nombre_virgule))```\nIl est de type `float` tout simplement.\n\n\n ## Liste\nLes listes, peuvent être un regroupement de chose.\nPrenons l'exemple de fruits :\n\n```py\nma_liste = [\"pomme\", \"banane\", \"orange\"]\nprint(ma_liste)```\n\nNous mettons des crochets puis on sépare les valeurs par des virgules.\nNous pouvons changer leurs valeurs celon ca position.\nIci voici les positions :\n\n```pomme: 0\nbanane: 1\norange: 2```\n\n\n**Attention** : On commence à 0. C'est l'index.\n\nChangeons par exemple le mot banane :\n\n```py\nma_liste = [\"pomme\", \"banane\", \"orange\"]\nprint(ma_liste)\nma_liste[1] = \"pêche\"\nprint(ma_liste)```\n\n\nNous avons aussi la fonction `len` qui est aussi très utile pour savoir le nombre de valeurs :\n\n```py\nma_liste = [\"pomme\", \"banane\", \"orange\"]\nprint(len(ma_liste))```\n\n\nIl va sortir **3**.\n\n## Tuple\nLes tuples ce sont exactement la même chose que les listes sauf que l'on ne peut pas changer les valeurs à moins de la convertir en liste via `list`.\nElles sont symbolisées par des parenthèses :\n```py\nle_tuple = (\"pomme\", \"banane\", \"orange\")\nprint(type(le_tuple))```",
            color=discord.Color.blue()
        )
        view=PyC.Cours2Button()
        await ch2.purge()
        await ch2.send(embed=embed, view=view)


        ch3_id = 1232425178210766860
        ch3 = self.get_channel(ch3_id)
        embed = discord.Embed(
            title="",
            description="# Les Conditions\n## If + Else\nPour réaliser, une condition nous allons utiliser les petits mots `if` et `else`.\nVoici un exemple :\n\n```py\ntemps = \"beau\"\nif temps == \"beau\":\n    print(\"Vous pouvez sortir dehors\")\nelse:\n    print(\"Vous devez rester à l'intérieur.\")```\n\nDans cet exemple, nous avons la condition: **Si le temps est égale à beau alors on écrit** `Vous pouvez sortir dehors.`\nNous utilisons `==` pour dire est égal. Si il est égal à beau la condition est rempli.\nSi la condition n'est pas rempli python ira dans le bloc `else` qui signifie `sinon`.\nEt donc il écrira : `Vous devez rester à l'intérieur.`\n\n## Elif\nNous avons aussi le mot `elif` qui est aussi à notre disposition.\nC'est la contraction de else + if = `elif`.\nIl permet de mettre d'autre condition entre le if et le else.\nVoici un exemple :\n\n```py\nage = input(\"Mettez votre âge :\")\nage = int(age) #Conversion en nombre\n\nif age > 100:\n    print(\"Vous êtes vieux\")\nelif age < 18:\n    print(\"Vous êtes mineur\")\nelse:\n    print(\"Vous êtes majeur\")```\n\n\nIci nous récupérons l'age de la personne.\nPuis nous ajoutons comme condition `elif age > 18:`.\nIl regardera si elle est vrai uniquement si l'âge de la personne n'est pas supérieur à 100.\nSi le elif n'est pas vrai il passera dans le `else`.",
            color=discord.Color.blue()
        )
        view=PyC.Cours3Button()
        await ch3.purge()
        await ch3.send(embed=embed, view=view)


        ch4_id = 1232425544075841628
        ch4 = self.get_channel(ch4_id)
        embed = discord.Embed(
            title="",
            description="# Boucles\n ## For\n ### Range\nLa boucle for combinée avec range permet de faire répéter un certain nombre de fois.\nVoici un exemple :\n\n```py\nfor nombre in range(5):\n    print(f\"Nous sommes au tour n°{nombre}\")\n```\n\nLa variable nombre contiendra le chiffre du nombre de tour.\nAttention : Il commence a 0 et le nombre écrit entre () n'est pas compté.\nCa donnera :\n\n```- 0\n- 1\n- 2\n- 3\n- 4```\n\nNous pouvons aussi définir a partir de quand il commence :\n\n```py\nfor nombre in range(1, 6):\n    print(nombre)\n```\n\nIl fera donc :\n\n```- 1\n- 2\n- 3\n- 4\n- 5```\n\n### Liste + For\nNous avons vu dans le cours précedent comment été faîtes les listes.\nGrâce à la boucle for nous pouvons voyager à l'intérieur.\n\n```py\nliste_fruits = [\"pomme\", \"banane\", \"orange\"]\nfor fruit in liste_fruits:\n    print(fruit)\n```\n\nNous definissons la liste.\nPuis pour la variable `fruit` dans la liste `liste_fruits`.\nEt ensuite on affiche fruit.\nQui contiendra successivement :\n\n```pomme\nbanane\norange```\n\n# While\nLa boucle `while` signifie pendant que suivi d'une condition si la condition est vrai la boucle refera un tour.\nSi elle est fausse elel s'arretera.\nVoici un exemple :\n\n```py\nreponse = \"\"\nwhile reponse == \"\":\n    reponse = input(\"Veuiller saisir quelque chose\")\n```\n\nIci nous definissons reponse à rien.\nPuis nous disons tant que reponse == \"\" alors tu demande à l'utilisateur de saisir quelque chose.\nGrâce à cette boucle nous obligeons l'utilisateur à saisir quelque chose.\nNous allons par exemple demander à l'utilisateur de saisir un nombre positif :\n\n```py\nnombre = -5\nwhile nombre < 0:\n    nombre = input(\"Veuiller saisir un nombre positif !\")\n    nombre = int(nombre) # Conversion en nombre\n    # Nous aurions pus aussi directement faire comme ca :\n    # int(input(\"Veuiller saisir un nombre positif !\"))\n```\n\nIci nous obligeons l'utilisateur à saisir un nombre positif.\n\nNous avons aussi de petit mot à notre disposition.\nNous avons par exemple `break` qui permet de terminer la boucle.\nVoici un exemple :\n\n```py\nfor x in range(0,10):\n    if x>5:\n        print(x)\n        break\n>>> 6```\nOu encore `continue`, il permet de passer directement au prochain élément de la boucle sans finir ce qu'il aurait du faire sur son passage (comme un skip).\nVoici un exemple :\n\n```py\nfor x in range(1,10):\n    if x%2==0: #verifie si il est pair\n        continue\n    print(x*5)\n>>> 5\n>>> 15\n>>> 25\n>>> 35\n>>> 45```",
            color=discord.Color.blue()
        )
        view=PyC.Cours4Button()
        await ch4.purge()
        await ch4.send(embed=embed, view=view)


        ch5_id = 1232425603546742784
        ch5 = self.get_channel(ch5_id)
        embed = discord.Embed(
            title="",
            description="# Fonctions\n## Fonction Base\nUne fonction permet de faire une suite d'action.\nElle doit être défini grâce au mot `def` puis ensuite être appellé.\nVoici un exemple :\n\n```py\ndef ma_fonction():\n    print(\"Salut tu vient d'appeller la fonction !\")\nmafonction()\n```\n\nSur les 2 premières lignes nous définissions ce qu'elle fait puis à la ligne 3, nous l'appellons.\nUne fonction peut aussi prendre des `arguments`.\nVoici un exemple :\n\n```py\ndef bonjour(nom, age):\n    print(f\"Salut {nom}, tu as {age} ans !\")\n```\n\nIci nous avons défini une fonction qui prend en paramètre un nom et un age.\nIci nous allons l'appellé :\n```py\nbonjour(nom=\"GoldJust\", age=20)\n```\n\n\n## Return\nUne fonction peut tout aussi bien retourner un résultat.\nVoici un exemple :\n\n```py\ndef addition(nombre1, nombre2):\n    resultat = nombre1 + nombre2\n    return resultat\n```\n\n\nVoici ici la définition de la fonction.\nElle prend en paramètre 2 nombres.\nLes additionnes et retourne le resultat.\nIci nous l'appellons :\n\n```py\nle_resultat = addition(5, 6)\nprint(le_resultat)\n\n>>> 11\n```",
            color=discord.Color.blue()
        )
        view=PyC.Cours5Button()
        await ch5.purge()
        await ch5.send(embed=embed, view=view)


        ch6_id = 1232425655065514075
        ch6 = self.get_channel(ch6_id)
        embed = discord.Embed(
            title="",
            description="# Modules\n\nLes modules en Python sont des fichiers contenant du code Python qui peuvent être importés dans d'autres programmes.\nIls permettent de regrouper des fonctionnalités similaires, d'organiser le code de manière modulaire et de favoriser la réutilisation du code.\n\n## Importation\n\nPour importer un module dans un programme Python, vous pouvez utiliser l'instruction `import` suivi du nom du module. Voici un exemple :\n```py\nimport os```\n\nCe code permet d'importer le module `os` qui contient la fonction `listdir` (qui permet de récupérer les fichiers/dossiers) ou encore `getcwd` (qui permet d'avoir le chemin absolu actuel).\nVous pouvez également importer des fonctions spécifiques d'un module pour les utiliser directement sans avoir à préfixer le nom du module. Par exemple :\n\n```py\nfrom os import listdir, getcwd```\n\nIci on importe uniquement ces fonctions.\n\n## Utilisation\n\nUne fois un module importé, vous pouvez utiliser les fonctions, les classes et les variables qu'il contient en utilisant un  `.`\n```py\n# Importation du module\nimport os\n\nchemin = os.getcwd()\nprint(f'Voici votre arborescence du chemin {chemin}:')\nfor file_dossier in os.listdir():\n    print(file_dossier)```\n\nSi vous avez besoin que de quelque fonction vous pouvez utiliser from. Voici un exemple :\n\n```py\n# Importation des fonctions du module\nfrom os import getcwd, listdir\n\nchemin = getcwd()\nprint(f'Voici votre arborescence du chemin {chemin}:')\nfor file_dossier in listdir():\n    print(file_dossier)```\n\nVous pouvez aussi utiliser `from module import *` l'étoile va importer toutes les fonctions.\nAttention cela peut entrainer des erreurs de nommage.\n\nIl existe aussi des `alias` pour pouvoir renommer les modules voici un exemple :\n\n```py\nimport discord as ds\nprint(ds.__version__)```\n\nIci on a renommé` discord` en `ds.`\n\n## Création de ses propres modules\n\nEn plus des modules intégrés de Python, vous pouvez créer vos propres modules personnalisés.\nPour ce faire, vous pouvez créer un fichier Python avec une extension .py et y placer le code que vous souhaitez regrouper.\n\nVoici un exemple :\n\n```py\n# Fichier mon_module.py\n\ndef addition(nombre_1, nombre_2) -> int:\n    return nombre_1 + nombre_2\n\ndef soustration(nombre_1, nombre_2) -> int:\n    return nombre_1 - nombre_2\n    \n# Ce code n'a aucune utilite c'est juste pour l'exemple```\n\nUtilisation de ces fonctions dans le programme principal :\n\n```py\n# Programme principal\nimport mon_module\n\nprint(mon_module.addition(1, 3))\nprint(mon_module.soustration(4, 9))```\n\nSi le module est dans un sous dossier, on utilise le `.` Voici un exemple :\n\nLe fichier mon_module.py a maintenant le chemin: `script/mon_module.py`\n\n```py\n# Programme principal \n\nimport script.mon_module # sans l'extension (le .py)\n#suite de ton code...```",
            color=discord.Color.blue()
        )
        view=PyC.Cours6Button()
        await ch6.purge()
        await ch6.send(embed=embed, view=view)

    async def JSCours(self):
        # Récupération de la catégorie
        ch1_id = 1232425775014350899
        ch1 = self.get_channel(ch1_id)
        embed = discord.Embed(
            title="",
            description="# Types de Variables\n\n## Introduction\n\nEn JavaScript, les variables peuvent contenir différents types de données, tels que des nombres, des chaînes de caractères, des booléens, des tableaux, des objets, etc. Comprendre les types de variables est essentiel pour travailler efficacement avec ce langage de programmation.\n\n## Types de Variables\n\n### 1. Nombre (Number)\n\nLes variables de type nombre stockent des valeurs numériques. Elles peuvent être des nombres entiers ou des nombres à virgule flottante.\n\nExemple :\n```javascript\nlet age = 25;\nlet prix = 9.99;\n```\n\n### 2. Chaîne de caractères (String)\n\nLes variables de type chaîne de caractères stockent du texte. Elles sont délimitées par des guillemets simples ('') ou doubles ("").\n\nExemple :\n```javascript\nlet nom = 'John';\nlet message = \"Bonjour, monde !\";\n```\n\n### 3. Booléen (Boolean)\n\nLes variables de type booléen ne peuvent avoir que deux valeurs : `true` (vrai) ou `false` (faux). Elles sont couramment utilisées pour les expressions logiques et les conditions.\n\nExemple :\n```javascript\nlet estVrai = true;\nlet estFaux = false;\n```\n\n### 4. Tableau (Array)\n\nLes variables de type tableau permettent de stocker plusieurs valeurs dans une seule variable. Les éléments du tableau peuvent être de différents types.\n\nExemple :\n```javascript\nlet fruits = ['pomme', 'banane', 'orange'];\nlet nombres = [1, 2, 3, 4, 5];\n```\n\n### 5. Objet (Object)\n\nLes variables de type objet permettent de regrouper plusieurs valeurs (appelées propriétés) et fonctions (ou méthodes) en une seule entité. Les objets sont fondamentaux en JavaScript.\n\nExemple :\n```javascript\nlet personne = {\n    nom: 'Alice',\n    age: 30,\n    adresse: '123 rue Principale',\n    direBonjour: function() {\n        console.log('Bonjour !');\n    }\n};\n```",
            color=discord.Color.blue()
        )
        view = JSC.Cours1Button()
        await ch1.purge()
        await ch1.send(embed=embed, view=view)


        ch2_id = 1232425854571643002
        ch2 = self.get_channel(ch2_id)
        embed = discord.Embed(
            title="",
            description="# Variables\n\n## Introduction\n\nTout d'abord, en JavaScript, toutes les phrases doivent se terminer par le symbole `;`\nEnsuite, les variables sont des éléments fondamentaux qui permettent de stocker et de manipuler des données. La déclaration de variables est une étape essentielle dans la programmation en JavaScript.\n\n## Déclaration de Variables\n\nEn JavaScript, il existe plusieurs façons de déclarer des variables. Voici les principales méthodes :\n\n### 1. Utilisation du mot-clé `let`\n\nLe mot-clé `let` est utilisé pour déclarer une variable pouvant être modifiée par la suite.\n\nExemple :\n```javascript\nlet age = 30;\nlet nom = \"John\";\n```\n\n### 2. Utilisation du mot-clé `const`\n\nLe mot-clé `const` est utilisé pour déclarer une variable dont la valeur ne peut pas être modifiée une fois qu'elle a été attribuée.\n\nExemple :\n```javascript\nconst PI = 3.14;\nconst nom = \"Alice\";\n```\n\n### 3. Utilisation du mot-clé `var` (déconseillé)\n\nLe mot-clé `var` était couramment utilisé pour déclarer des variables avant l'introduction de `let` et `const`. Cependant, il est maintenant déconseillé de l'utiliser en raison de son comportement ambigu par rapport à la portée des variables.\n\nExemple :\n```javascript\nvar x = 5;\nvar y = \"hello\";\n```\n\n## Règles de Nommage des Variables\n\nEn JavaScript, les variables peuvent être nommées selon certaines règles :\n\n- Le nom des variables peut contenir des lettres, des chiffres, des caractères de soulignement (_) et des signes dollar ($).\n- Le nom des variables doit commencer par une lettre, un signe dollar ou un caractère de soulignement.\n- Les variables sont sensibles à la casse, ce qui signifie que `nom` et `Nom` sont deux variables différentes.\n- Les noms de variables ne doivent pas être des mots clés du langage JavaScript.\n\nExemple :\n```javascript\nlet nomUtilisateur = \"Alice\";\nlet ageUtilisateur = 30;\n```\n\n## Conclusion\n\nLa déclaration de variables en JavaScript est une étape fondamentale dans la programmation. En utilisant les mots-clés `let`, `const` et `var`, ainsi que les règles de nommage appropriées, vous pouvez créer et manipuler des variables efficacement dans vos programmes JavaScript.",
            color=discord.Color.blue()
        )
        view=JSC.Cours2Button()
        await ch2.purge()
        await ch2.send(embed=embed, view=view)


        ch3_id = 1232425915321946233
        ch3 = self.get_channel(ch3_id)
        embed = discord.Embed(
            title="",
            description="# Conditions\n\n## Introduction\n\nLes conditions sont des structures de contrôle fondamentales en programmation. En JavaScript, les conditions permettent d'exécuter des blocs de code en fonction de l'évaluation de certaines expressions logiques. Comprendre les conditions est essentiel pour écrire des programmes JavaScript efficaces et flexibles.\n\n## Les Structures Conditionnelles\n\nEn JavaScript, il existe plusieurs structures conditionnelles qui permettent de contrôler le flux d'exécution du code. Les principales structures conditionnelles sont les suivantes :\n\n### 1. L'instruction `if`\n\nL'instruction `if` permet d'exécuter un bloc de code si une condition est vraie (true).\n\nExemple :\n```javascript\nlet x = 10;\nif (x > 5) {\n    console.log(\"x est supérieur à 5\");\n}\n```\n\n### 2. L'instruction `if...else`\n\nL'instruction `if...else` permet d'exécuter un bloc de code si une condition est vraie, sinon un autre bloc de code est exécuté.\n\nExemple :\n```javascript\nlet x = 3;\nif (x > 5) {\n    console.log(\"x est supérieur à 5\");\n} else {\n    console.log(\"x est inférieur ou égal à 5\");\n}\n```\n\n### 3. L'instruction `\"if...else if...else\"`\n\nL'instruction `if...else if...else` permet d'exécuter un bloc de code parmi plusieurs blocs alternatifs en fonction de différentes conditions.\n\nExemple :\n```javascript\nlet x = 10;\nif (x > 10) {\n    console.log(\"x est supérieur à 10\");\n} else if (x < 10) {\n    console.log(\"x est inférieur à 10\");\n} else {\n    console.log(\"x est égal à 10\");\n}\n```\n\n### 4. L'opérateur ternaire (condition ? expression1 : expression2)\n\nL'opérateur ternaire est une forme concise d'instruction conditionnelle qui permet d'écrire une condition en une seule ligne.\n\nExemple :\n```javascript\nlet x = 10;\nlet message = (x > 5) ? \"x est supérieur à 5\" : \"x est inférieur ou égal à 5\";\nconsole.log(message);\n```\n\n## Conclusion\n\nLes conditions sont des éléments fondamentaux en programmation JavaScript. En utilisant les structures conditionnelles telles que `if`, `if...else`, `if...else if...else` et l'opérateur ternaire, vous pouvez contrôler le flux d'exécution de votre code en fonction des différentes conditions logiques. Cela vous permet de créer des programmes JavaScript flexibles et adaptatifs.",
            color=discord.Color.blue()
        )
        view=JSC.Cours3Button()
        await ch3.purge()
        await ch3.send(embed=embed, view=view)


        ch4_id = 1232425973887275018
        ch4 = self.get_channel(ch4_id)
        embed = discord.Embed(
            title="",
            description="# Boucles\n\n## Introduction\n\nLes boucles sont des structures de contrôle qui permettent d'exécuter un bloc de code plusieurs fois. En JavaScript, il existe plusieurs types de boucles, chacune ayant ses propres caractéristiques et utilisations.\n\n## Les Boucles en JavaScript\n\n### 1. La Boucle `for`\n\nLa boucle `for` permet d'exécuter un bloc de code un nombre spécifié de fois. Elle est souvent utilisée lorsque le nombre d'itérations est connu à l'avance.\n\nExemple :\n```javascript\nfor (let i = 0; i < 5; i++) {\n    console.log(\"Tour numéro \" + i);\n}\n```\n\n### 2. La Boucle `while`\n\nLa boucle `while` permet d'exécuter un bloc de code tant qu'une condition spécifiée est vraie. Elle est souvent utilisée lorsque le nombre d'itérations n'est pas connu à l'avance.\n\nExemple :\n```javascript\nlet i = 0;\nwhile (i < 5) {\n    console.log(\"Tour numéro \" + i);\n    i++;\n}\n```\n\n### 3. La Boucle `do...while`\n\nLa boucle `do...while` est similaire à la boucle `while`, mais elle garantit que le bloc de code est exécuté au moins une fois avant de vérifier la condition.\n\nExemple :\n```javascript\nlet i = 0;\ndo {\n    console.log(\"Tour numéro \" + i);\n    i++;\n} while (i < 5);\n```\n\n## Les Instructions de Contrôle des Boucles\n\nEn JavaScript, il existe plusieurs instructions de contrôle qui permettent de modifier le comportement des boucles :\n\n- L'instruction `break` permet de sortir de la boucle immédiatement.\n- L'instruction `continue` permet de passer à l'itération suivante de la boucle.\n- L'instruction `return` permet de sortir de la fonction (dans le cas des fonctions).\n\nExemple :\n```javascript\nfor (let i = 0; i < 10; i++) {\n    if (i === 5) {\n        break; // Sort de la boucle lorsque i est égal à 5\n    }\n    if (i % 2 === 0) {\n        continue; // Passe à l'itération suivante si i est pair\n    }\n    console.log(i);\n}\n```\n\n## Conclusion\n\nLes boucles sont des éléments fondamentaux en programmation JavaScript. En utilisant les boucles `for`, `while` et `do...while`, ainsi que les instructions de contrôle associées, vous pouvez effectuer des opérations répétitives de manière efficace et flexible dans vos programmes JavaScript.",
            color=discord.Color.blue()
        )
        view=JSC.Cours4Button()
        await ch4.purge()
        await ch4.send(embed=embed, view=view)


        ch5_id = 1232426038789804133
        ch5 = self.get_channel(ch5_id)
        embed = discord.Embed(
            title="",
            description="# Fonctions\n\n## Introduction\n\nLes fonctions sont des blocs de code réutilisables qui permettent d'effectuer des tâches spécifiques. En JavaScript, les fonctions sont des éléments fondamentaux de la programmation, et elles offrent de nombreux avantages en termes de modularité, de réutilisabilité et de maintenabilité du code.\n\n## Déclaration de Fonctions\n\nEn JavaScript, il existe plusieurs façons de déclarer des fonctions. Voici les principales méthodes :\n\n### 1. Déclaration de fonction nommée\n\nLa méthode la plus courante consiste à déclarer une fonction nommée à l'aide du mot-clé `function`.\n\nExemple :\n```javascript\nfunction maFonction() {\n    // Bloc de code à exécuter\n    console.log(\"Bonjour !\");\n}\n```\n\n### 2. Expression de fonction anonyme\n\nIl est également possible de déclarer une fonction anonyme en l'assignant à une variable.\n\nExemple :\n```javascript\nlet maFonction = function() {\n    // Bloc de code à exécuter\n    console.log(\"Bonjour !\");\n};\n```\n\n### 3. Fonction fléchée (Arrow Function)\n\nLes fonctions fléchées sont une syntaxe plus concise pour déclarer des fonctions anonymes.\n\nExemple :\n```javascript\nlet maFonction = () => {\n    // Bloc de code à exécuter\n    console.log(\"Bonjour !\");\n};\n```\n\n## Appel de Fonctions\n\nUne fois qu'une fonction est déclarée, elle peut être appelée (ou invoquée) pour exécuter son bloc de code.\n\nExemple :\n```javascript\nmaFonction(); // Appel de la fonction\n```\n\n## Paramètres et Arguments\n\nLes fonctions peuvent accepter des paramètres, qui sont des valeurs passées à la fonction lors de son appel. Ces paramètres sont utilisés à l'intérieur de la fonction pour effectuer des opérations.\n\nExemple :\n```javascript\nfunction addition(a, b) {\n    let resultat = a + b;\n    console.log(resultat);\n}\n\naddition(5, 3); // Appel de la fonction avec des arguments\n```\n\n## Valeur de Retour\n\nLes fonctions peuvent également renvoyer une valeur à l'endroit où elles ont été appelées à l'aide du mot-clé `return`.\n\nExemple :\n```javascript\nfunction addition(a, b) {\n    return a + b;\n}\n\nlet resultat = addition(5, 3); // Appel de la fonction et récupération du résultat\nconsole.log(resultat);\n```\n\n## Conclusion\n\nLes fonctions sont des éléments essentiels de la programmation JavaScript. En utilisant les différentes méthodes de déclaration de fonctions, ainsi que les paramètres, les arguments et les valeurs de retour, vous pouvez créer des blocs de code réutilisables et modulaires qui améliorent la lisibilité et la maintenabilité de votre code JavaScript.",
            color=discord.Color.blue()
        )
        view=JSC.Cours5Button()
        await ch5.purge()
        await ch5.send(embed=embed, view=view)


        ch6_id = 1232426078744875059
        ch6 = self.get_channel(ch6_id)
        embed = discord.Embed(
            title="",
            description=f"# Modules\n\n## Introduction\n\nL'importation en JavaScript permet d'inclure des fonctionnalités d'autres fichiers ou modules dans un fichier JavaScript actuel. Cette fonctionnalité est essentielle pour organiser et réutiliser le code de manière modulaire.\n\n## Importation de modules\n\nEn JavaScript, les modules sont des fichiers individuels qui exportent des fonctionnalités, des variables ou des classes pour être utilisés dans d'autres fichiers. Voici comment importer des modules dans un fichier JavaScript :\n\n### Utilisation de l'instruction `import`\n\nL'instruction `import` est utilisée pour importer des fonctionnalités spécifiques d'un module.\n\nExemple :\n```javascript\nimport {{ fonction1, fonction2 }} from \'./module.js\';\n```\n\n### Importation d'un module entier\n\nIl est également possible d'importer tout un module en utilisant l'étoile (*) suivi du nom du module.\n\nExemple :\n```javascript\nimport * as monModule from \'./module.js\';```\n\n### Importation par défaut\n\nCertains modules ont une exportation par défaut, qui peut être importée sans utiliser de syntaxe d'accolades.\n\nExemple :\n```javascript\nimport maFonction from \'./module.js\';\n```\n\n### Utilisation de l'instruction `require`\n\nL'instruction `require` est une autre méthode pour importer des modules en JavaScript, principalement utilisée dans les environnements Node.js.\n\nExemple :\n```javascript\nconst module = require('discord.js');```\n## Utilisation des Fonctionnalités Importées\n\nUne fois les fonctionnalités importées, vous pouvez les utiliser dans votre fichier JavaScript comme n'importe quelle autre fonction ou variable.\n\nExemple :\n```javascript\nfonction1();\nfonction2();\n```\n\n## Conclusion\n\nL'importation en JavaScript est un moyen puissant d'organiser et de réutiliser le code de manière modulaire. En utilisant l'instruction `import` ou `require`, vous pouvez inclure des fonctionnalités d'autres fichiers ou modules dans votre code, ce qui facilite la gestion de projets complexes et la réutilisation du code.",
            color=discord.Color.blue()
        )
        view=JSC.Cours6Button()
        await ch6.purge()
        await ch6.send(embed=embed, view=view)
    
    async def TicketMsg(self):
        TicketChannel = self.get_channel(1196557781214449738)
        
        # Récupérer les messages dans le canal
        async for message in TicketChannel.history(limit=None):
            if message.author == self.user and message.embeds:
                embed = message.embeds[0]
                if embed.title == "Ticket":
                    await message.delete()  # Supprimer le message existant avec le titre "Ticket"
        
        # Envoyer le nouveau message
        embed = discord.Embed(
            title="Ticket",
            description="Besoin d'aide ? Ouvrez un ticket !\n🗒️ Recrutements --> Ouvre un ticket pour être recruté !\n🤝 Partenariats --> Ouvre un ticket pour faire une collaboration !\n❓ Support --> Pose une question !", 
            color=discord.Color.blue())
        await TicketChannel.send(embed=embed, view=TC.TicketView(self, interaction=None))


    async def on_ready(self):
        # await bot.change_presence(activity=discord.Game(name="!help"))
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/help_bot"))
        table = Table()
        
        table.add_column(f"Bot {bot.user} fonctionne parfaitement", justify="center", style="cyan", no_wrap=True)
        
        # ligne1 = Text(f"ID: {bot.user.id}", justify="center", style="bold red")
        ligne1 = Text(justify="center")
        ligne1.append("ID: ", style="bold red")
        ligne1.append(f"{bot.user.id}", style="bold Magenta")
        
        # ligne2 = Text(f"Version de Discord: {discord.__version__}", justify="center", style="bold red")
        ligne2 = Text(justify="center")
        ligne2.append("Version de Discord: ", style="bold red")
        ligne2.append(f"{discord.__version__}", style="bold Magenta")
        
        # ligne3 = Text(f"Connecté en tant que {bot.user.name} avec {len(bot.shards)} shards.", justify="center", style="bold red")
        ligne3 = Text(justify="center")
        ligne3.append("Connecté en tant que ", style="bold red")
        ligne3.append(f"{bot.user.name}", style="bold Magenta")
        ligne3.append(" avec ", style="bold red")
        # ligne3.append(f"{len(bot.shards)}", style="bold Magenta")
        # ligne3.append(" shards.", style="bold red")
        
        table.add_row(ligne1)
        table.add_row(ligne2)
        table.add_row(ligne3,end_section=True)
        # ajout d'une ligne de séparation --------------------

        # ligne4 = Text(f"Actuellement sur {len(bot.guilds)} serveurs:", justify="left", style="bold blue")
        ligne4 = Text(justify="left")
        ligne4.append("Actuellement sur ", style="bold blue")
        ligne4.append(f"{len(bot.guilds)}", style="bold cyan")
        ligne4.append(" serveurs:", style="bold blue")
        table.add_row(ligne4)

        for server in bot.guilds:
            # ligne5 = Text(f" - {server.name} (ID: {server.id})", justify="left", style="bold blue")
            ligne5 = Text(justify="left")
            ligne5.append(" - ", style="bold blue")
            ligne5.append(server.name, style="bold cyan")
            ligne5.append(f" (ID: ", style="bold blue")
            ligne5.append(f"{server.id}", style="bold cyan")
            ligne5.append(")", style="bold blue")
            table.add_row(ligne5)
        table.add_row(end_section=True)
        # for server in bot.guilds:
        #     table.add_row(f" - {server.name} (ID: {server.id})",end_section=True)
        await self.load_cogs(self, table, excluded_cogs_list)
        
        
        ligne10 = Text(f"Syncing slash commands:", justify="left", style="bold dark_yellow")
        try:
            synced = await bot.tree.sync()
            # Liste all slash commands
            table.add_row(ligne10)  # Ajouter l'en-tête une fois avant la boucle

            for command in synced:
                ligne11 = Text(justify="left")
                ligne11.append(" - ", style="bold dark_yellow")
                ligne11.append(command.name, style="bold bright_yellow")
                ligne11.append(" (ID: ", style="bold dark_yellow")
                ligne11.append(f"{command.id}", style="bold bright_yellow")
                ligne11.append(")", style="bold dark_yellow")
                
                table.add_row(ligne11)  # Ajouter chaque commande dans la boucle

            table.add_row(end_section=True)  # Fin de section après la boucle
        except Exception as e:
            print(e)
            
        await self.start_task_after_table_display(bot)
        await self.TicketMsg()
        await self.PythonCours()
        await self.JSCours()
        console = Console()
        console.print(table)



    async def start_task_after_table_display(self, bot: commands.AutoShardedBot):
        my_cog_instance = bot.get_cog('tasks')
        if my_cog_instance:
            my_cog_instance.message_send_task.start()  # Démarrage de la tâche après l'affichage du tableau


    async def init_db(self) -> None:
        async with aiosqlite.connect(
            f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
        ) as db:
            with open(
                f"{os.path.realpath(os.path.dirname(__file__))}/database/schema.sql"
            ) as file:
                await db.executescript(file.read())
            await db.commit()

    async def load_cogs(self, bot, table, excluded_cogs):
        ligne6 = Text(f"Chargement des cogs:", justify="left", style="bold green")
        table.add_row(ligne6)
        for filename in os.listdir('./cogs'):
            if (filename in excluded_cogs):
                continue
            if (filename.endswith('.py') and not filename.startswith('__') and 
                not any(excluded_string in filename for excluded_string in excluded_cogs)):
                cog_name = filename[:-3]  # Retirer .py
                try:
                    # Importer le module du cog
                    cog_module = __import__(f"cogs.{cog_name}", fromlist=[cog_name])
                    
                    # Obtenir la classe du cog
                    cog_class = getattr(cog_module, cog_name, None)
                    
                    # Vérifier si la classe du cog existe et l'ajouter au bot
                    if callable(cog_class):
                        await bot.add_cog(cog_class(bot))
                        ligne6 = Text(justify="left")
                        ligne6.append(" - ", style="bold green")
                        ligne6.append(f"{cog_name}", style="bold green3s")
                        ligne6.append(" chargé avec succès", style="bold green")
                    else:
                        raise Exception(f"Le cog {cog_name} n'a pas de classe correspondante.")
                    
                    table.add_row(ligne6)
                except Exception as e:
                    ligne7 = Text(justify="left")
                    ligne7.append(" - ", style="bold red")
                    ligne7.append(f"{cog_name}", style="bold bright_red")
                    ligne7.append(" n'a pas pu être chargé: ", style="bold red")
                    ligne7.append(str(e), style="bold bright_red")
                    table.add_row(ligne7)
                    print(e)


    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:
        """
        Setup the game status task of the bot.
        """
        statuses = ["/help"]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

    @status_task.before_loop
    async def before_status_task(self) -> None:
        """
        Before starting the status changing task, we make sure the bot is ready
        """
        await self.wait_until_ready()

    async def setup_hook(self) -> None:
        """
        This will just be executed when the bot starts the first time.
        """
        self.logger.info(f"Logged in as {self.user.name}")
        self.logger.info(f"discord.py API version: {discord.__version__}")
        self.logger.info(f"Python version: {platform.python_version()}")
        self.logger.info(
            f"Running on: {platform.system()} {platform.release()} ({os.name})"
        )
        self.logger.info("-------------------")
        await self.init_db()
        self.status_task.start()
        self.database = DatabaseManager(
            connection=await aiosqlite.connect(
                f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
            )
        )

    async def on_message(self, message: discord.Message) -> None:
        """
        The code in this event is executed every time someone sends a message, with or without the prefix

        :param message: The message that was sent.
        """
        if message.author == self.user:
            return

        if message.content.startswith("!"):
            await message.delete()

        if message.channel == bot.get_channel(1229912237091852339):
            await message.channel.send("<@&1229528607786008626>")

        if message.author.id == 302050872383242240:  # ID de Disboard
            if message.channel == bot.get_channel(1229180297346809967): # salon de bump
                current_time = datetime.now(pytz.utc) + timedelta(seconds=7200)
                timestamp = int(current_time.timestamp())
                await message.channel.send(f"Il sera temps de bumper dans <t:{timestamp}:R>")
                print("Le serveur vient d'être bumpé")
                await asyncio.sleep(7200)  # Attendre 2 heures (7200 secondes)
                await message.channel.send(f"<@1124611079855673355>, <@694873777942691920>, il est temps de bumper à nouveau !")

        await self.process_commands(message)
        
    async def on_command_completion(self, context: Context) -> None:
        """
        The code in this event is executed every time a normal command has been *successfully* executed.

        :param context: The context of the command that has been executed.
        """
        full_command_name = context.command.qualified_name
        split = full_command_name.split(" ")
        executed_command = str(split[0])
        if context.guild is not None:
            self.logger.info(
                f"Executed {executed_command} command in {context.guild.name} (ID: {context.guild.id}) by {context.author} (ID: {context.author.id})"
            )
        else:
            self.logger.info(
                f"Executed {executed_command} command by {context.author} (ID: {context.author.id}) in DMs"
            )

    async def on_command_error(self, context: Context, error) -> None:
        """
        The code in this event is executed every time a normal valid command catches an error.

        :param context: The context of the normal command that failed executing.
        :param error: The error that has been faced.
        """
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(error.retry_after, 60)
            hours, minutes = divmod(minutes, 60)
            hours = hours % 24
            embed = discord.Embed(
                description=f"**Please slow down** - You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                description="You are not the owner of the bot!", color=0xE02B2B
            )
            await context.send(embed=embed)
            if context.guild:
                self.logger.warning(
                    f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the guild {context.guild.name} (ID: {context.guild.id}), but the user is not an owner of the bot."
                )
            else:
                self.logger.warning(
                    f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the bot's DMs, but the user is not an owner of the bot."
                )
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description="You are missing the permission(s) `"
                + ", ".join(error.missing_permissions)
                + "` to execute this command!",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                description="I am missing the permission(s) `"
                + ", ".join(error.missing_permissions)
                + "` to fully perform this command!",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Error!",
                # We need to capitalize because the command arguments have no capital letter in the code and they are the first word in the error message.
                description=str(error).capitalize(),
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        else:
            raise error

    async def on_message_delete(self, message: discord.Message):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est supprimé.

        :param message: Le message qui a été supprimé.
        """
        author_id = message.author.id
        author_mention = message.author.mention
        content = message.content
        channel_name = message.channel.name
        channel_mention = message.channel.mention
        print(f"Message supprimé - Contenu: {content}, Auteur ID: {author_id}  /  {message.author.name}, Salon: {channel_name}")
        embed = discord.Embed(
            title="Message supprimé !",
            description=f"Contenu : {content}\nAuteur : {author_id}  /  {author_mention}\nSalon : {channel_mention}",
            color=0xff0000
            )
        if not content.startswith("!") or not message.channel.id in [1231276908759613521, 1232049659757727896]:
            await self.get_channel(1231276908759613521).send(embed=embed)

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est modifié.

        :param before: Le message avant la modification.
        :param after: Le message après la modification.
        """
        # Vérifie si l'auteur du message avant la modification est un bot
        if before.author.bot:
            return
        
        author_id = before.author.id
        author_mention = before.author.mention
        content_before = before.content
        content_after = after.content
        channel_name = before.channel.name
        channel_mention = before.channel.mention
        print(f"Message modifié - Contenu avant: {content_before}, Contenu après: {content_after}, Auteur ID: {author_id}  /  {before.author.name}, Salon: {channel_name}")
        embed = discord.Embed(
            title="Message modifié !",
            description=f"Contenu avant : {content_before}\nContenu après : {content_after}\nAuteur : {author_id}  /  {author_mention}\nSalon : {channel_mention}",
            color=0xff0000
            )
        await self.get_channel(1231276908759613521).send(embed=embed)


    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est modifié.

        :param before: Le message avant la modification.
        :param after: Le message après la modification.
        """

        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if entry.target == user:
                print(f"Utilisateur banni - {user.id}  /  {user.name} à été banni de {guild.name} par {entry.user}")
                embed = discord.Embed(
                    title="Utilisateur banni !",
                    description=f"{user.id}  /  {user.mention} à été banni de {guild.name} par {entry.user}",
                    color=0xff0000
                    )
                await self.get_channel(1231276908759613521).send(embed=embed)

    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est modifié.

        :param before: Le message avant la modification.
        :param after: Le message après la modification.
        """
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.unban):
            if entry.target == user:
                print(f"Utilisateur débanni - {user.id}  /  {user.name} à été débanni de {guild.name} par {entry.user}")
                embed = discord.Embed(
                    title="Utilisateur débanni !",
                    description=f"{user.id}  /  {user.mention} à été débanni de {guild.name} par {entry.user}",
                    color=0xff0000
                    )
                await self.get_channel(1231276908759613521).send(embed=embed)

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 1232081955605184616:  # ID du message embed
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            emoji = str(payload.emoji)

            roles_emojis = {
                '<:c_:1232075318345597020>': 1231952778553987215,
                '<:css:1232074095986872360>': 1231952923366264863,
                '<:python:1232075302398591046>': 1231952273492672593,
                '<:php:1232075285629763675>': 1232048720623702077,
                '<:html:1232069038386057338>': 1231952881100263434,
                '<:js:1232072012411961458>': 1231952694697267229
            }

            role_id = roles_emojis.get(emoji)
            if role_id:
                role = guild.get_role(role_id)
                await member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 1232081955605184616:  # ID du message embed
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            emoji = str(payload.emoji)

            roles_emojis = {
                '<:c_:1232075318345597020>': 1231952778553987215,
                '<:css:1232074095986872360>': 1231952923366264863,
                '<:python:1232075302398591046>': 1231952273492672593,
                '<:php:1232075285629763675>': 1232048720623702077,
                '<:html:1232069038386057338>': 1231952881100263434,
                '<:js:1232072012411961458>': 1231952694697267229
            }

            role_id = roles_emojis.get(emoji)
            if role_id:
                role = guild.get_role(role_id)
                await member.remove_roles(role)

load_dotenv()

bot = DiscordBot()
bot.run("MTIyODM5ODMyODY1NjU2NDM3NQ.GFBbua.YRDqM-CjgHNIAOVqLoCQBnN8PBTh99OHauhppU")
