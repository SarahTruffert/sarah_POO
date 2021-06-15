
# Part2

Un petit peu de norme :/
Quelque petites erreur mais sinon c'est propre !


# Army

Ligne 25 ce n'est pas str() qu'il faut utiliser mais isinstance.

Sinon pas mal !

# Battlefield

Evite les nom de fonction en francais :) mais c'est pas tres grave.
Ligne 12 and co, on compare une class en utilisant `is` ou `isinstance` mais pas `==`
Sinon c'est cool !

# Warlord & Defender

C'est dommage d'avoir dupliquer le comportement de la defense, ca fait 2 fois plus de code a maintenir.
Comment peut tu eviter cela ?

# Knight & Vampire

Pour le knight et le vampire, redeclare un attribut `_alive` ? Il n'existe pas chez warrior ?


