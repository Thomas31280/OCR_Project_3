Le programme est à exécuter depuis le fichier main_file.py. Ce script utilise deux dépendances ; txt_interpretor.py et constant_storage.py.
On retrouvera un fichier requirements.txt à jour qui permet, via un pip install -r requirements dans la console, d'installer toutes les
librairies nécessaires à l'exécution du programme.

Il s'agit d'un programme à "interface graphique interactive" qui se base sur pygame ( adaptation de SDL pour le langage Python ) pour la gestion
de la partie graphique. L'interaction avec le programme se fait avec les flèches directionnelles. Il s'exécutera tant que l'utilisateur ne ferme
pas la fenêtre pygame. Des informations complémentaires seront transmises dans la console au cours de l'exécution. La répartition des items à
ramasser se fait aléatoirement, et la structure logique du programme lui permet une modularité assez large. Avec pour leviers d'action
constant_storage.py, items.txt, path_builder.txt, starting_characters_position.txt et le contenu du dossier display, il sera possible, sans
modification dans main_file.py ni dans txt_interpretor.py de changer la taille du labyrinthe, les dimensions de la fenêtre, le nombre de sprites,
la position initiales des personnages, et même la structure du labyrinthe ( sous réserve de respecter la structure des données évidemment ! ).
Le programme s'adaptera de manière automatique à tous ces changements ( pourvu qu'ils soient cohérents ).

Enfin, notons que des messages d'avertissement de niveau de log Warning seront affichés dans la console par pygame au lancement du programme.
Ces flags sont liés à l'exécution d'opérations à l'intérieur des window.blit(), mais sont sans aucune conséquence dans l'exécution du programme.
Ce "problème" serait assez délicat ( mais possible, plus ou moins proprement ) à régler en raison de la structure logique du programme, mais
présente peu d'intérêt compte tenu du fait qu'il vient plutôt de la librairie pygame...