## Exercice 1

Définir une classe **Date** pour représenter uen date, avec trois attributs **jour**, **mois** et **année**.

### Question 1

Ecrire son constructeur.

### Question 2

Ajouter une méthode **\_\_str__** qui renvoie une chaîne de caractères de la forme *"11 novembre 1918"*. On pourra se servir d'un attribut de classe qui est un tableau donnant des douze mois de l'année. Tester en construisant des objets de la classe **Date** puis en les affichant avec print.

### Question 3

Ajouter une méthode **\_\_lt__** qui permet de déterminer si une date **d1** est antérieure à une date **d2** en écrivant **d1<d2**.

## Exercice 2

Définir une classe **Fraction** pour représenter un nombre rationnel. Cette classe possède deux attributs, **num** et **denom**, qui sont des entiers et désignent respectivement le numérateur et le dénominateur soit plus particulièrement un entier strictement positif.

### Question 1

Ecrire le constructeur de cette classe. Le constructeur doit lever une **ValueError** si le dénominateur fourni n'est pas strictement positif.

### Question 2

Ajouter une méthode **\_\_str__** qui renvoie une chaîne de caractères de la forme *"12 / 35"*, ou simplement de la forme *"12"* lorsque le dénominateur vaut un.

### Question 3

Ajouter des méthodes **\_\_eq__** et **\_\_lt__** qui reçoivent une deuxième fraction en argument et renvoie True si la première fraction représente respectivement un nombre égal ou un nombre strictement inférieur à la deuxième fraction.

### Question 4

Ajouter des méthodes **\_\_add__** et **\_\_mul__** qui reçoivent une deuxième fraction en argument et renvoient une nouvelle fraction représentant respectivement la somme et le produit des deux fractions.

### Question 5

Tester ces opérations.

### Question 6

Bonus: s'assurer que les fractions sont toujours sous forme réduite.
