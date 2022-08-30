// EXERISE 1

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log("Affichage du tableaux");
console.log(fruits);

//Supprimez Banana de la baie.
fruits.shift();
console.log("Affichage du tableaux après suppression de 'Banana' ");
console.log(fruits);

//Triez le tableau par ordre alphabétique.
fruits.sort();
console.log("Affichage du tableaux après trie");
console.log(fruits);

//Ajoutez "Kiwi" à la fin du tableau.
fruits.push('Kiwi');
console.log("Affichage du tableaux après ajoue de 'Kiwi' ");
console.log(fruits);

//Supprimez "Apples" du tableau. N'utilisez pas la même méthode que dans la partie 1.
fruits.splice(0,1);
console.log("Affichage du tableaux après suppressions de 'Apples");
console.log(fruits);

//Triez le tableau dans l'ordre inverse. (Pas alphabétique, mais inversez le tableau actuel, c'est-à-dire que ['a', 'c', 'b'] devient ['b', 'c', 'a'])
fruits.reverse();
console.log("Affichage du tableaux après inversion de l'ordre");
console.log(fruits);

//************************************************************

//EXERCISE 2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log("Affichage du tableaux");
console.log(moreFruits);
console.log("Affichage de 'Orange'");
console.log(moreFruits[1][1][0]);
