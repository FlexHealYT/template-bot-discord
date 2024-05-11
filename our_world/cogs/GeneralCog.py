import platform
import random
import asyncio
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

import cours.PythonCog as PyC
import cours.JSCog as JSC
import cours.PHPCog as PHPC
import cours.HTMLCog as HTMLC
import cours.C_Cog as CC
import cours.CSSCog as CSSC


class GeneralCog(commands.Cog, name="general"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.context_menu_user = app_commands.ContextMenu(
            name="Obtenir l'ID", callback=self.grab_id
        )
        self.bot.tree.add_command(self.context_menu_user)
        self.context_menu_message = app_commands.ContextMenu(
            name="Supprimer les spoilers", callback=self.remove_spoilers
        )
        self.bot.tree.add_command(self.context_menu_message)
        
    @commands.hybrid_command(
            name="js_cours",
            description="Envoie les cours de js"
    )
    @commands.has_permissions(administrator=True)
    async def js_cours(self, ctx: Context) -> None:
        # Récupération de la catégorie
        ch1_id = 1232425775014350899
        ch1 = self.bot.get_channel(ch1_id)
        embed = discord.Embed(
            title="",
            description="# Types de Variables\n\n## Introduction\n\nEn JavaScript, les variables peuvent contenir différents types de données, tels que des nombres, des chaînes de caractères, des booléens, des tableaux, des objets, etc. Comprendre les types de variables est essentiel pour travailler efficacement avec ce langage de programmation.\n\n## Types de Variables\n\n### 1. Nombre (Number)\n\nLes variables de type nombre stockent des valeurs numériques. Elles peuvent être des nombres entiers ou des nombres à virgule flottante.\n\nExemple :\n```javascript\nlet age = 25;\nlet prix = 9.99;\n```\n\n### 2. Chaîne de caractères (String)\n\nLes variables de type chaîne de caractères stockent du texte. Elles sont délimitées par des guillemets simples ('') ou doubles ("").\n\nExemple :\n```javascript\nlet nom = 'John';\nlet message = \"Bonjour, monde !\";\n```\n\n### 3. Booléen (Boolean)\n\nLes variables de type booléen ne peuvent avoir que deux valeurs : `true` (vrai) ou `false` (faux). Elles sont couramment utilisées pour les expressions logiques et les conditions.\n\nExemple :\n```javascript\nlet estVrai = true;\nlet estFaux = false;\n```\n\n### 4. Tableau (Array)\n\nLes variables de type tableau permettent de stocker plusieurs valeurs dans une seule variable. Les éléments du tableau peuvent être de différents types.\n\nExemple :\n```javascript\nlet fruits = ['pomme', 'banane', 'orange'];\nlet nombres = [1, 2, 3, 4, 5];\n```\n\n### 5. Objet (Object)\n\nLes variables de type objet permettent de regrouper plusieurs valeurs (appelées propriétés) et fonctions (ou méthodes) en une seule entité. Les objets sont fondamentaux en JavaScript.\n\nExemple :\n```javascript\nlet personne = {\n    nom: 'Alice',\n    age: 30,\n    adresse: '123 rue Principale',\n    direBonjour: function() {\n        console.log('Bonjour !');\n    }\n};\n```",
            color=discord.Color.blue()
        )
        view = JSC.Cours1Button()
        await ch1.purge()
        await ch1.send(embed=embed, view=view)


        ch2_id = 1232425854571643002
        ch2 = self.bot.get_channel(ch2_id)
        embed = discord.Embed(
            title="",
            description="# Variables\n\n## Introduction\n\nTout d'abord, en JavaScript, toutes les phrases doivent se terminer par le symbole `;`\nEnsuite, les variables sont des éléments fondamentaux qui permettent de stocker et de manipuler des données. La déclaration de variables est une étape essentielle dans la programmation en JavaScript.\n\n## Déclaration de Variables\n\nEn JavaScript, il existe plusieurs façons de déclarer des variables. Voici les principales méthodes :\n\n### 1. Utilisation du mot-clé `let`\n\nLe mot-clé `let` est utilisé pour déclarer une variable pouvant être modifiée par la suite.\n\nExemple :\n```javascript\nlet age = 30;\nlet nom = \"John\";\n```\n\n### 2. Utilisation du mot-clé `const`\n\nLe mot-clé `const` est utilisé pour déclarer une variable dont la valeur ne peut pas être modifiée une fois qu'elle a été attribuée.\n\nExemple :\n```javascript\nconst PI = 3.14;\nconst nom = \"Alice\";\n```\n\n### 3. Utilisation du mot-clé `var` (déconseillé)\n\nLe mot-clé `var` était couramment utilisé pour déclarer des variables avant l'introduction de `let` et `const`. Cependant, il est maintenant déconseillé de l'utiliser en raison de son comportement ambigu par rapport à la portée des variables.\n\nExemple :\n```javascript\nvar x = 5;\nvar y = \"hello\";\n```\n\n## Règles de Nommage des Variables\n\nEn JavaScript, les variables peuvent être nommées selon certaines règles :\n\n- Le nom des variables peut contenir des lettres, des chiffres, des caractères de soulignement (_) et des signes dollar ($).\n- Le nom des variables doit commencer par une lettre, un signe dollar ou un caractère de soulignement.\n- Les variables sont sensibles à la casse, ce qui signifie que `nom` et `Nom` sont deux variables différentes.\n- Les noms de variables ne doivent pas être des mots clés du langage JavaScript.\n\nExemple :\n```javascript\nlet nomUtilisateur = \"Alice\";\nlet ageUtilisateur = 30;\n```\n\n## Conclusion\n\nLa déclaration de variables en JavaScript est une étape fondamentale dans la programmation. En utilisant les mots-clés `let`, `const` et `var`, ainsi que les règles de nommage appropriées, vous pouvez créer et manipuler des variables efficacement dans vos programmes JavaScript.",
            color=discord.Color.blue()
        )
        view=JSC.Cours2Button()
        await ch2.purge()
        await ch2.send(embed=embed, view=view)


        ch3_id = 1232425915321946233
        ch3 = self.bot.get_channel(ch3_id)
        embed = discord.Embed(
            title="",
            description="# Conditions\n\n## Introduction\n\nLes conditions sont des structures de contrôle fondamentales en programmation. En JavaScript, les conditions permettent d'exécuter des blocs de code en fonction de l'évaluation de certaines expressions logiques. Comprendre les conditions est essentiel pour écrire des programmes JavaScript efficaces et flexibles.\n\n## Les Structures Conditionnelles\n\nEn JavaScript, il existe plusieurs structures conditionnelles qui permettent de contrôler le flux d'exécution du code. Les principales structures conditionnelles sont les suivantes :\n\n### 1. L'instruction `if`\n\nL'instruction `if` permet d'exécuter un bloc de code si une condition est vraie (true).\n\nExemple :\n```javascript\nlet x = 10;\nif (x > 5) {\n    console.log(\"x est supérieur à 5\");\n}\n```\n\n### 2. L'instruction `if...else`\n\nL'instruction `if...else` permet d'exécuter un bloc de code si une condition est vraie, sinon un autre bloc de code est exécuté.\n\nExemple :\n```javascript\nlet x = 3;\nif (x > 5) {\n    console.log(\"x est supérieur à 5\");\n} else {\n    console.log(\"x est inférieur ou égal à 5\");\n}\n```\n\n### 3. L'instruction `\"if...else if...else\"`\n\nL'instruction `if...else if...else` permet d'exécuter un bloc de code parmi plusieurs blocs alternatifs en fonction de différentes conditions.\n\nExemple :\n```javascript\nlet x = 10;\nif (x > 10) {\n    console.log(\"x est supérieur à 10\");\n} else if (x < 10) {\n    console.log(\"x est inférieur à 10\");\n} else {\n    console.log(\"x est égal à 10\");\n}\n```\n\n### 4. L'opérateur ternaire (condition ? expression1 : expression2)\n\nL'opérateur ternaire est une forme concise d'instruction conditionnelle qui permet d'écrire une condition en une seule ligne.\n\nExemple :\n```javascript\nlet x = 10;\nlet message = (x > 5) ? \"x est supérieur à 5\" : \"x est inférieur ou égal à 5\";\nconsole.log(message);\n```\n\n## Conclusion\n\nLes conditions sont des éléments fondamentaux en programmation JavaScript. En utilisant les structures conditionnelles telles que `if`, `if...else`, `if...else if...else` et l'opérateur ternaire, vous pouvez contrôler le flux d'exécution de votre code en fonction des différentes conditions logiques. Cela vous permet de créer des programmes JavaScript flexibles et adaptatifs.",
            color=discord.Color.blue()
        )
        view=JSC.Cours3Button()
        await ch3.purge()
        await ch3.send(embed=embed, view=view)


        ch4_id = 1232425973887275018
        ch4 = self.bot.get_channel(ch4_id)
        embed = discord.Embed(
            title="",
            description="# Boucles\n\n## Introduction\n\nLes boucles sont des structures de contrôle qui permettent d'exécuter un bloc de code plusieurs fois. En JavaScript, il existe plusieurs types de boucles, chacune ayant ses propres caractéristiques et utilisations.\n\n## Les Boucles en JavaScript\n\n### 1. La Boucle `for`\n\nLa boucle `for` permet d'exécuter un bloc de code un nombre spécifié de fois. Elle est souvent utilisée lorsque le nombre d'itérations est connu à l'avance.\n\nExemple :\n```javascript\nfor (let i = 0; i < 5; i++) {\n    console.log(\"Tour numéro \" + i);\n}\n```\n\n### 2. La Boucle `while`\n\nLa boucle `while` permet d'exécuter un bloc de code tant qu'une condition spécifiée est vraie. Elle est souvent utilisée lorsque le nombre d'itérations n'est pas connu à l'avance.\n\nExemple :\n```javascript\nlet i = 0;\nwhile (i < 5) {\n    console.log(\"Tour numéro \" + i);\n    i++;\n}\n```\n\n### 3. La Boucle `do...while`\n\nLa boucle `do...while` est similaire à la boucle `while`, mais elle garantit que le bloc de code est exécuté au moins une fois avant de vérifier la condition.\n\nExemple :\n```javascript\nlet i = 0;\ndo {\n    console.log(\"Tour numéro \" + i);\n    i++;\n} while (i < 5);\n```\n\n## Les Instructions de Contrôle des Boucles\n\nEn JavaScript, il existe plusieurs instructions de contrôle qui permettent de modifier le comportement des boucles :\n\n- L'instruction `break` permet de sortir de la boucle immédiatement.\n- L'instruction `continue` permet de passer à l'itération suivante de la boucle.\n- L'instruction `return` permet de sortir de la fonction (dans le cas des fonctions).\n\nExemple :\n```javascript\nfor (let i = 0; i < 10; i++) {\n    if (i === 5) {\n        break; // Sort de la boucle lorsque i est égal à 5\n    }\n    if (i % 2 === 0) {\n        continue; // Passe à l'itération suivante si i est pair\n    }\n    console.log(i);\n}\n```\n\n## Conclusion\n\nLes boucles sont des éléments fondamentaux en programmation JavaScript. En utilisant les boucles `for`, `while` et `do...while`, ainsi que les instructions de contrôle associées, vous pouvez effectuer des opérations répétitives de manière efficace et flexible dans vos programmes JavaScript.",
            color=discord.Color.blue()
        )
        view=JSC.Cours4Button()
        await ch4.purge()
        await ch4.send(embed=embed, view=view)


        ch5_id = 1232426038789804133
        ch5 = self.bot.get_channel(ch5_id)
        embed = discord.Embed(
            title="",
            description="# Fonctions\n\n## Introduction\n\nLes fonctions sont des blocs de code réutilisables qui permettent d'effectuer des tâches spécifiques. En JavaScript, les fonctions sont des éléments fondamentaux de la programmation, et elles offrent de nombreux avantages en termes de modularité, de réutilisabilité et de maintenabilité du code.\n\n## Déclaration de Fonctions\n\nEn JavaScript, il existe plusieurs façons de déclarer des fonctions. Voici les principales méthodes :\n\n### 1. Déclaration de fonction nommée\n\nLa méthode la plus courante consiste à déclarer une fonction nommée à l'aide du mot-clé `function`.\n\nExemple :\n```javascript\nfunction maFonction() {\n    // Bloc de code à exécuter\n    console.log(\"Bonjour !\");\n}\n```\n\n### 2. Expression de fonction anonyme\n\nIl est également possible de déclarer une fonction anonyme en l'assignant à une variable.\n\nExemple :\n```javascript\nlet maFonction = function() {\n    // Bloc de code à exécuter\n    console.log(\"Bonjour !\");\n};\n```\n\n### 3. Fonction fléchée (Arrow Function)\n\nLes fonctions fléchées sont une syntaxe plus concise pour déclarer des fonctions anonymes.\n\nExemple :\n```javascript\nlet maFonction = () => {\n    // Bloc de code à exécuter\n    console.log(\"Bonjour !\");\n};\n```\n\n## Appel de Fonctions\n\nUne fois qu'une fonction est déclarée, elle peut être appelée (ou invoquée) pour exécuter son bloc de code.\n\nExemple :\n```javascript\nmaFonction(); // Appel de la fonction\n```\n\n## Paramètres et Arguments\n\nLes fonctions peuvent accepter des paramètres, qui sont des valeurs passées à la fonction lors de son appel. Ces paramètres sont utilisés à l'intérieur de la fonction pour effectuer des opérations.\n\nExemple :\n```javascript\nfunction addition(a, b) {\n    let resultat = a + b;\n    console.log(resultat);\n}\n\naddition(5, 3); // Appel de la fonction avec des arguments\n```\n\n## Valeur de Retour\n\nLes fonctions peuvent également renvoyer une valeur à l'endroit où elles ont été appelées à l'aide du mot-clé `return`.\n\nExemple :\n```javascript\nfunction addition(a, b) {\n    return a + b;\n}\n\nlet resultat = addition(5, 3); // Appel de la fonction et récupération du résultat\nconsole.log(resultat);\n```\n\n## Conclusion\n\nLes fonctions sont des éléments essentiels de la programmation JavaScript. En utilisant les différentes méthodes de déclaration de fonctions, ainsi que les paramètres, les arguments et les valeurs de retour, vous pouvez créer des blocs de code réutilisables et modulaires qui améliorent la lisibilité et la maintenabilité de votre code JavaScript.",
            color=discord.Color.blue()
        )
        view=JSC.Cours5Button()
        await ch5.purge()
        await ch5.send(embed=embed, view=view)


        ch6_id = 1232426078744875059
        ch6 = self.bot.get_channel(ch6_id)
        embed = discord.Embed(
            title="",
            description=f"# Modules\n\n## Introduction\n\nL'importation en JavaScript permet d'inclure des fonctionnalités d'autres fichiers ou modules dans un fichier JavaScript actuel. Cette fonctionnalité est essentielle pour organiser et réutiliser le code de manière modulaire.\n\n## Importation de modules\n\nEn JavaScript, les modules sont des fichiers individuels qui exportent des fonctionnalités, des variables ou des classes pour être utilisés dans d'autres fichiers. Voici comment importer des modules dans un fichier JavaScript :\n\n### Utilisation de l'instruction `import`\n\nL'instruction `import` est utilisée pour importer des fonctionnalités spécifiques d'un module.\n\nExemple :\n```javascript\nimport {{ fonction1, fonction2 }} from \'./module.js\';\n```\n\n### Importation d'un module entier\n\nIl est également possible d'importer tout un module en utilisant l'étoile (*) suivi du nom du module.\n\nExemple :\n```javascript\nimport * as monModule from \'./module.js\';```\n\n### Importation par défaut\n\nCertains modules ont une exportation par défaut, qui peut être importée sans utiliser de syntaxe d'accolades.\n\nExemple :\n```javascript\nimport maFonction from \'./module.js\';\n```\n\n### Utilisation de l'instruction `require`\n\nL'instruction `require` est une autre méthode pour importer des modules en JavaScript, principalement utilisée dans les environnements Node.js.\n\nExemple :\n```javascript\nconst module = require('discord.js');```\n## Utilisation des Fonctionnalités Importées\n\nUne fois les fonctionnalités importées, vous pouvez les utiliser dans votre fichier JavaScript comme n'importe quelle autre fonction ou variable.\n\nExemple :\n```javascript\nfonction1();\nfonction2();\n```\n\n## Conclusion\n\nL'importation en JavaScript est un moyen puissant d'organiser et de réutiliser le code de manière modulaire. En utilisant l'instruction `import` ou `require`, vous pouvez inclure des fonctionnalités d'autres fichiers ou modules dans votre code, ce qui facilite la gestion de projets complexes et la réutilisation du code.",
            color=discord.Color.blue()
        )
        view=JSC.Cours6Button()
        await ch6.purge()
        await ch6.send(embed=embed, view=view)


    @commands.hybrid_command(
            name="python_cours",
            description="Envoie les cours de python"
    )
    @commands.has_permissions(administrator=True)
    async def python_cours(self, ctx: Context) -> None:
        # Récupération de la catégorie
        ch1_id = 1232425069184286740
        ch1 = self.bot.get_channel(ch1_id)
        embed = discord.Embed(
            title="",
            description="# Variables\n## **C'est quoi une variable ?**\nNous allons voir aujourd'hui, les **variables**.\nPour commencer, une variable c'est comme une boîte où l'on stocke une information.\nCette information peut-être un texte appellé **chaine de caractère (string)**.\nOu, elle peut contenir un **nombre entier simple (integer)**.\n\n## **Variables en python**\nPour, en python, définir une variable, il faut qu'il n'y ai pas d'espace, ni de caractere speciaux sauf le underscore `_`.\nPar exemple, ici nous allons definir une variable prenom :\n```py\nprenom = \"GoldJust\"```\nNous mettons `GoldJust` entre guillemets entre \" car c'est une **chaine de caractère**.\nSi nous voulons afficher cette variable dans le terminal, nous allons utiliser la fonction `print()`\nPour utiliser une cette fonction, nous lui mettons en paramètre la variable ce qui donne :\n```py\nprenom = \"GoldJust\"\nprint(prenom)```\nSi nous voudrions définir un âge nous mettrons `age = 5`, le 5 **sans** guillemet car c'est un chiffre.\nSi, nous voulons par exemple afficher une phrase avec la variable age et la variable prenom, nous allons faire comme ceci :\n```py\nprenom = \"GoldJust\"\nage = 20\nprint(f\"Le membre {prenom} a {age} ans !\")```\nLe petit f sert a dire que ce qu'il y a entre les {} ce sera des variables.\nIl existe plusieurs manière de faire ça, notament avec des `+` ou encore des `,`.\nNous pouvons aussi changer la valeur d'une variable.\n```py\nprenom = \"GoldJust\"\nprint(prenom)\nprenom = \"Gold\"\nprint(prenom)```\nPython ecrira au debut `GoldJust` puis ensuite `Gold` car la valeur a changé.\n\n## **Input en python**\nVous pourrez avoir envie de demander son âge et son prénom à l'utilisateur.\nPour cela, nous allons utiliser la fonction `input()` qui permet de faire saisir à l'utilisateur quelque chose.\nVoici un exemple :\n```py\nprenom = input(\"Qu\'elle est votre prenom: \")\nage = input(\"Qu\'elle est votre age : \")\nage = int(age)\nage_suivant = age+1\nprint(f\"Bonjour {prenom}, l'année prochaine vous aurez {age_suivant} !\")```\nRemarquez qu'on utilise la fonction int à la ligne `3`, car l'input renvoie une chaine de caractère même si c'est un chiffre.\nPour le convertir en nombre, nous utilisons donc cette fonction.\nPuis, nous créons une nouvelle variable appelée `age_suivant` qui contient l'age saisi + 1.\nEnsuite, nous affichons le tout via un `print`.",
            color=discord.Color.blue()
        )
        view = PyC.Cours1Button()
        await ch1.purge()
        await ch1.send(embed=embed, view=view)


        ch2_id = 1232424986946572349
        ch2 = self.bot.get_channel(ch2_id)
        embed = discord.Embed(
            title="",
            description="# Types de variables\n## String\nLe string est une chaine de caractère, en voici un exemple:\n```py\nchaine = \"Salut \"```\nIl est de type `str`.\nOn peut le voir via la fonction type :```py\nchaine = \"Salut \"\nprint(type(chaine))```\n\n\nOn peut utiliser la fonction str pour convertir un nombre en chaine :```py\nnombre = 5\nchaine = str(nombre)\nprint(type(nombre))\nprint(type(chaine))\n```\n\n## Integer\nUn `integer` est un chiffre entier.\n```py\nmon_nombre = 5\nprint(type(mon_nombre))\n```\nCa donnera en type `int`.\nPour convertir une chaine de caractère en nombre on peut utiliser la fonction int.\n**Attention** : La chaine doit être un chiffre entre \".```py\nchaine = \"5\"\nnombre = int(chaine)\nprint(type(chaine))\nprint(type(nombre))```\n\nCette fonction peut être utile pour les additions / soustractions.\n## Float\nUn `float` est un nombre à virgule.\nPour symboliser cette virgule nous utilisons le point :\n```py\nnombre_virgule = 5.5\nprint(type(nombre_virgule))```\nIl est de type `float` tout simplement.\n\n\n ## Liste\nLes listes, peuvent être un regroupement de chose.\nPrenons l'exemple de fruits :\n\n```py\nma_liste = [\"pomme\", \"banane\", \"orange\"]\nprint(ma_liste)```\n\nNous mettons des crochets puis on sépare les valeurs par des virgules.\nNous pouvons changer leurs valeurs celon ca position.\nIci voici les positions :\n\n```pomme: 0\nbanane: 1\norange: 2```\n\n\n**Attention** : On commence à 0. C'est l'index.\n\nChangeons par exemple le mot banane :\n\n```py\nma_liste = [\"pomme\", \"banane\", \"orange\"]\nprint(ma_liste)\nma_liste[1] = \"pêche\"\nprint(ma_liste)```\n\n\nNous avons aussi la fonction `len` qui est aussi très utile pour savoir le nombre de valeurs :\n\n```py\nma_liste = [\"pomme\", \"banane\", \"orange\"]\nprint(len(ma_liste))```\n\n\nIl va sortir **3**.\n\n## Tuple\nLes tuples ce sont exactement la même chose que les listes sauf que l'on ne peut pas changer les valeurs à moins de la convertir en liste via `list`.\nElles sont symbolisées par des parenthèses :\n```py\nle_tuple = (\"pomme\", \"banane\", \"orange\")\nprint(type(le_tuple))```",
            color=discord.Color.blue()
        )
        view=PyC.Cours2Button()
        await ch2.purge()
        await ch2.send(embed=embed, view=view)


        ch3_id = 1232425178210766860
        ch3 = self.bot.get_channel(ch3_id)
        embed = discord.Embed(
            title="",
            description="# Les Conditions\n## If + Else\nPour réaliser, une condition nous allons utiliser les petits mots `if` et `else`.\nVoici un exemple :\n\n```py\ntemps = \"beau\"\nif temps == \"beau\":\n    print(\"Vous pouvez sortir dehors\")\nelse:\n    print(\"Vous devez rester à l'intérieur.\")```\n\nDans cet exemple, nous avons la condition: **Si le temps est égale à beau alors on écrit** `Vous pouvez sortir dehors.`\nNous utilisons `==` pour dire est égal. Si il est égal à beau la condition est rempli.\nSi la condition n'est pas rempli python ira dans le bloc `else` qui signifie `sinon`.\nEt donc il écrira : `Vous devez rester à l'intérieur.`\n\n## Elif\nNous avons aussi le mot `elif` qui est aussi à notre disposition.\nC'est la contraction de else + if = `elif`.\nIl permet de mettre d'autre condition entre le if et le else.\nVoici un exemple :\n\n```py\nage = input(\"Mettez votre âge :\")\nage = int(age) #Conversion en nombre\n\nif age > 100:\n    print(\"Vous êtes vieux\")\nelif age < 18:\n    print(\"Vous êtes mineur\")\nelse:\n    print(\"Vous êtes majeur\")```\n\n\nIci nous récupérons l'age de la personne.\nPuis nous ajoutons comme condition `elif age > 18:`.\nIl regardera si elle est vrai uniquement si l'âge de la personne n'est pas supérieur à 100.\nSi le elif n'est pas vrai il passera dans le `else`.",
            color=discord.Color.blue()
        )
        view=PyC.Cours3Button()
        await ch3.purge()
        await ch3.send(embed=embed, view=view)


        ch4_id = 1232425544075841628
        ch4 = self.bot.get_channel(ch4_id)
        embed = discord.Embed(
            title="",
            description="# Boucles\n ## For\n ### Range\nLa boucle for combinée avec range permet de faire répéter un certain nombre de fois.\nVoici un exemple :\n\n```py\nfor nombre in range(5):\n    print(f\"Nous sommes au tour n°{nombre}\")\n```\n\nLa variable nombre contiendra le chiffre du nombre de tour.\nAttention : Il commence a 0 et le nombre écrit entre () n'est pas compté.\nCa donnera :\n\n```- 0\n- 1\n- 2\n- 3\n- 4```\n\nNous pouvons aussi définir a partir de quand il commence :\n\n```py\nfor nombre in range(1, 6):\n    print(nombre)\n```\n\nIl fera donc :\n\n```- 1\n- 2\n- 3\n- 4\n- 5```\n\n### Liste + For\nNous avons vu dans le cours précedent comment été faîtes les listes.\nGrâce à la boucle for nous pouvons voyager à l'intérieur.\n\n```py\nliste_fruits = [\"pomme\", \"banane\", \"orange\"]\nfor fruit in liste_fruits:\n    print(fruit)\n```\n\nNous definissons la liste.\nPuis pour la variable `fruit` dans la liste `liste_fruits`.\nEt ensuite on affiche fruit.\nQui contiendra successivement :\n\n```pomme\nbanane\norange```\n\n# While\nLa boucle `while` signifie pendant que suivi d'une condition si la condition est vrai la boucle refera un tour.\nSi elle est fausse elel s'arretera.\nVoici un exemple :\n\n```py\nreponse = \"\"\nwhile reponse == \"\":\n    reponse = input(\"Veuiller saisir quelque chose\")\n```\n\nIci nous definissons reponse à rien.\nPuis nous disons tant que reponse == \"\" alors tu demande à l'utilisateur de saisir quelque chose.\nGrâce à cette boucle nous obligeons l'utilisateur à saisir quelque chose.\nNous allons par exemple demander à l'utilisateur de saisir un nombre positif :\n\n```py\nnombre = -5\nwhile nombre < 0:\n    nombre = input(\"Veuiller saisir un nombre positif !\")\n    nombre = int(nombre) # Conversion en nombre\n    # Nous aurions pus aussi directement faire comme ca :\n    # int(input(\"Veuiller saisir un nombre positif !\"))\n```\n\nIci nous obligeons l'utilisateur à saisir un nombre positif.\n\nNous avons aussi de petit mot à notre disposition.\nNous avons par exemple `break` qui permet de terminer la boucle.\nVoici un exemple :\n\n```py\nfor x in range(0,10):\n    if x>5:\n        print(x)\n        break\n>>> 6```\nOu encore `continue`, il permet de passer directement au prochain élément de la boucle sans finir ce qu'il aurait du faire sur son passage (comme un skip).\nVoici un exemple :\n\n```py\nfor x in range(1,10):\n    if x%2==0: #verifie si il est pair\n        continue\n    print(x*5)\n>>> 5\n>>> 15\n>>> 25\n>>> 35\n>>> 45```",
            color=discord.Color.blue()
        )
        view=PyC.Cours4Button()
        await ch4.purge()
        await ch4.send(embed=embed, view=view)


        ch5_id = 1232425603546742784
        ch5 = self.bot.get_channel(ch5_id)
        embed = discord.Embed(
            title="",
            description="# Fonctions\n## Fonction Base\nUne fonction permet de faire une suite d'action.\nElle doit être défini grâce au mot `def` puis ensuite être appellé.\nVoici un exemple :\n\n```py\ndef ma_fonction():\n    print(\"Salut tu vient d'appeller la fonction !\")\nmafonction()\n```\n\nSur les 2 premières lignes nous définissions ce qu'elle fait puis à la ligne 3, nous l'appellons.\nUne fonction peut aussi prendre des `arguments`.\nVoici un exemple :\n\n```py\ndef bonjour(nom, age):\n    print(f\"Salut {nom}, tu as {age} ans !\")\n```\n\nIci nous avons défini une fonction qui prend en paramètre un nom et un age.\nIci nous allons l'appellé :\n```py\nbonjour(nom=\"GoldJust\", age=20)\n```\n\n\n## Return\nUne fonction peut tout aussi bien retourner un résultat.\nVoici un exemple :\n\n```py\ndef addition(nombre1, nombre2):\n    resultat = nombre1 + nombre2\n    return resultat\n```\n\n\nVoici ici la définition de la fonction.\nElle prend en paramètre 2 nombres.\nLes additionnes et retourne le resultat.\nIci nous l'appellons :\n\n```py\nle_resultat = addition(5, 6)\nprint(le_resultat)\n\n>>> 11\n```",
            color=discord.Color.blue()
        )
        view=PyC.Cours5Button()
        await ch5.purge()
        await ch5.send(embed=embed, view=view)


        ch6_id = 1232425655065514075
        ch6 = self.bot.get_channel(ch6_id)
        embed = discord.Embed(
            title="",
            description="# Modules\n\nLes modules en Python sont des fichiers contenant du code Python qui peuvent être importés dans d'autres programmes.\nIls permettent de regrouper des fonctionnalités similaires, d'organiser le code de manière modulaire et de favoriser la réutilisation du code.\n\n## Importation\n\nPour importer un module dans un programme Python, vous pouvez utiliser l'instruction `import` suivi du nom du module. Voici un exemple :\n```py\nimport os```\n\nCe code permet d'importer le module `os` qui contient la fonction `listdir` (qui permet de récupérer les fichiers/dossiers) ou encore `getcwd` (qui permet d'avoir le chemin absolu actuel).\nVous pouvez également importer des fonctions spécifiques d'un module pour les utiliser directement sans avoir à préfixer le nom du module. Par exemple :\n\n```py\nfrom os import listdir, getcwd```\n\nIci on importe uniquement ces fonctions.\n\n## Utilisation\n\nUne fois un module importé, vous pouvez utiliser les fonctions, les classes et les variables qu'il contient en utilisant un  `.`\n```py\n# Importation du module\nimport os\n\nchemin = os.getcwd()\nprint(f'Voici votre arborescence du chemin {chemin}:')\nfor file_dossier in os.listdir():\n    print(file_dossier)```\n\nSi vous avez besoin que de quelque fonction vous pouvez utiliser from. Voici un exemple :\n\n```py\n# Importation des fonctions du module\nfrom os import getcwd, listdir\n\nchemin = getcwd()\nprint(f'Voici votre arborescence du chemin {chemin}:')\nfor file_dossier in listdir():\n    print(file_dossier)```\n\nVous pouvez aussi utiliser `from module import *` l'étoile va importer toutes les fonctions.\nAttention cela peut entrainer des erreurs de nommage.\n\nIl existe aussi des `alias` pour pouvoir renommer les modules voici un exemple :\n\n```py\nimport discord as ds\nprint(ds.__version__)```\n\nIci on a renommé` discord` en `ds.`\n\n## Création de ses propres modules\n\nEn plus des modules intégrés de Python, vous pouvez créer vos propres modules personnalisés.\nPour ce faire, vous pouvez créer un fichier Python avec une extension .py et y placer le code que vous souhaitez regrouper.\n\nVoici un exemple :\n\n```py\n# Fichier mon_module.py\n\ndef addition(nombre_1, nombre_2) -> int:\n    return nombre_1 + nombre_2\n\ndef soustration(nombre_1, nombre_2) -> int:\n    return nombre_1 - nombre_2\n    \n# Ce code n'a aucune utilite c'est juste pour l'exemple```\n\nUtilisation de ces fonctions dans le programme principal :\n\n```py\n# Programme principal\nimport mon_module\n\nprint(mon_module.addition(1, 3))\nprint(mon_module.soustration(4, 9))```\n\nSi le module est dans un sous dossier, on utilise le `.` Voici un exemple :\n\nLe fichier mon_module.py a maintenant le chemin: `script/mon_module.py`\n\n```py\n# Programme principal \n\nimport script.mon_module # sans l'extension (le .py)\n#suite de ton code...```",
            color=discord.Color.blue()
        )
        view=PyC.Cours6Button()
        await ch6.purge()
        await ch6.send(embed=embed, view=view)


    @commands.hybrid_command(
            name="requis",
            description="envoie le message des prérequis"
    )
    @commands.is_owner()
    async def requis(self, ctx: Context) -> None:
        embed = discord.Embed(
            title="Visual Studio Code",
            description=f"Pour coder, nous aurons besoin d'un éditeur de code appeler **IDE**.\nPersonnellement, je vous conseilles Visual Studio Code.\nNous allons voir comment l'installer.\n\nRendez vous sur ce site: [installer VSCode](<https://code.visualstudio.com/docs/?dv=win>)\n\nUne fois l'éxécutable téléchargé. Double cliquez dessus.\nEt installer le comme une application normale.\nUne fois installer, lancez-le.",
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/640px-Visual_Studio_Code_1.35_icon.svg.png"
)
        await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="help", description="Liste toutes les commandes du bot."
    )
    async def help(self, context: Context) -> None:
        prefix = self.bot.config["prefix"]
        embed = discord.Embed(
            title="Aide", description="Liste des commandes disponibles :", color=0xBEBEFE
        )
        for cog_name in self.bot.cogs:
            if cog_name == "owner" and not await self.bot.is_owner(context.author):
                continue
            cog = self.bot.get_cog(cog_name.lower())
            if cog is not None:
                commands = cog.get_commands()
                if commands:
                    data = []
                    for command in commands:
                        description = command.description.partition("\n")[0]
                        data.append(f"/{command.name} - {description}")
                    help_text = "\n".join(data)
                    embed.add_field(
                        name=cog_name.capitalize(), value=f"```{help_text}```", inline=False
                    )
        await context.send(embed=embed, ephemeral=True)



    # Message context menu command
    async def remove_spoilers(
        self, interaction: discord.Interaction, message: discord.Message
    ) -> None:
        """
        Supprime les spoilers du message. Cette commande nécessite l'intention MESSAGE_CONTENT pour fonctionner correctement.

        :param interaction: L'interaction de la commande d'application.
        :param message: Le message avec lequel l'interaction a lieu.
        """
        spoiler_attachment = None
        for attachment in message.attachments:
            if attachment.is_spoiler():
                spoiler_attachment = attachment
                break
        embed = discord.Embed(
            title="Message sans spoilers",
            description=message.content.replace("||", ""),
            color=0xBEBEFE,
        )
        if spoiler_attachment is not None:
            embed.set_image(url=attachment.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # User context menu command
    async def grab_id(
        self, interaction: discord.Interaction, user: discord.User
    ) -> None:
        """
        Récupère l'ID de l'utilisateur.

        :param interaction: L'interaction de la commande d'application.
        :param user: L'utilisateur avec lequel l'interaction a lieu.
        """
        embed = discord.Embed(
            description=f"L'ID de {user.mention} est `{user.id}`.",
            color=0xBEBEFE,
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="infobot",
        description="Obtenez des informations utiles (ou non) sur le bot.",
    )
    async def botinfo(self, context: Context) -> None:
        """
        Obtenez des informations utiles (ou non) sur le bot.

        :param context: Le contexte de la commande hybride.
        """
        embed = discord.Embed(
            description="Utilisé le modèle de [Krypton](https://krypton.ninja)",
            color=0xBEBEFE,
        )
        embed.set_author(name="Informations sur le bot")
        embed.add_field(name="Propriétaire :", value="flexheal_ytb#0606", inline=True)
        embed.add_field(
            name="Version Python :", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(
            name="Préfixe:",
            value=f"/ (Commandes Slash) ou {self.bot.config['prefix']} pour les commandes normales",
            inline=False,
        )
        embed.set_footer(text=f"Demandé par {context.author}")
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="infoserv",
        description="Obtenez des informations utiles (ou non) sur le serveur.",
    )
    async def serverinfo(self, context: Context) -> None:
        """
        Obtenez des informations utiles (ou non) sur le serveur.

        :param context: Le contexte de la commande hybride.
        """
        roles = [role.name for role in context.guild.roles]
        num_roles = len(roles)
        if num_roles > 50:
            roles = roles[:50]
            roles.append(f">>>> Affichage [50/{num_roles}] Rôles")
        roles = ", ".join(roles)

        embed = discord.Embed(
            title="**Nom du Serveur :**", description=f"{context.guild}", color=0xBEBEFE
        )
        if context.guild.icon is not None:
            embed.set_thumbnail(url=context.guild.icon.url)
        embed.add_field(name="ID du Serveur", value=context.guild.id)
        embed.add_field(name="Nombre de Membres", value=context.guild.member_count)
        embed.add_field(
            name="Salons Textuels/Vocaux", value=f"{len(context.guild.channels)}"
        )
        embed.add_field(name=f"Rôles ({len(context.guild.roles)})", value=roles)
        embed.set_footer(text=f"Créé le : {context.guild.created_at}")
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="ping",
        description="Vérifiez si le bot est en ligne.",
    )
    async def ping(self, context: Context) -> None:
        """
        Vérifiez si le bot est en ligne.

        :param context: Le contexte de la commande hybride.
        """
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"La latence du bot est {round(self.bot.latency * 1000)}ms.",
            color=0xBEBEFE,
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="8ball",
        description="Posez n'importe quelle question au bot.",
    )
    @app_commands.describe(question="La question que vous voulez poser.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Posez n'importe quelle question au bot.

        :param context: Le contexte de la commande hybride.
        :param question: La question que l'utilisateur devrait poser.
        """
        answers = [
            "C'est certain.",
            "Il en est décidément ainsi.",
            "Vous pouvez compter dessus.",
            "Sans aucun doute.",
            "Oui - absolument.",
            "Comme je le vois, oui.",
            "Très probablement.",
            "Les perspectives sont bonnes.",
            "Oui.",
            "Les signes indiquent oui.",
            "Réessayez plus tard.",
            "Demandez à nouveau plus tard.",
            "Mieux vaut ne pas vous le dire maintenant.",
            "Impossible de prédire maintenant.",
            "Concentrez-vous et demandez à nouveau plus tard.",
            "Ne comptez pas dessus.",
            "Ma réponse est non.",
            "Mes sources disent non.",
            "Les perspectives ne semblent pas bonnes.",
            "Très douteux.",
        ]
        embed = discord.Embed(
            title="**Ma réponse :**",
            description=f"{random.choice(answers)}",
            color=0xBEBEFE,
        )
        embed.set_footer(text=f"La question était : {question}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="Obtenez le prix actuel du bitcoin.",
    )
    async def bitcoin(self, context: Context) -> None:
        """
        Obtenez le prix actuel du bitcoin.

        :param context: Le contexte de la commande hybride.
        """
        # Cela empêchera votre bot de tout arrêter lors de la réalisation d'une requête Web - voir: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json()  # Pour une raison quelconque, le contenu retourné est de type JavaScript
                    embed = discord.Embed(
                        title="Prix du Bitcoin",
                        description=f"Le prix actuel est de {data['bpi']['USD']['rate_float']}$ !",
                        color=0xBEBEFE,
                    )
                else:
                    embed = discord.Embed(
                        title="Erreur!",
                        description="Quelque chose ne va pas avec l'API, veuillez réessayer plus tard",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(GeneralCog(bot))
