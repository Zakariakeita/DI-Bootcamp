//Exercise 1
    console.log("Exercise 1 : ");
    //Stockez votre nourriture préférée dans une variable.
    let food = "Foutou Banane";

    //Enregistrez votre repas préféré de la journée dans une variable (c'est-à-dire petit-déjeuner, déjeuner ou dîner)
    let meal= "Lunch";

    //Affichage du resultat
    console.log("Affichage du resultat");
    console.log("I eat " +food + " at every "+ meal);


//****************************************************
//Exercise 2
    //Part 1
    console.log("Exercise 2 : ");
    console.log("Part 1 : ");
    //Using this array 
    let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
    console.log("Affichage de mes series");
    console.log(myWatchedSeries);

    //Créez une variable myWatchedSeriesLengthdont le nom est égal au nombre de séries dans le myWatchedSeriestableau.
    let myWatchedSeriesLengthdont= myWatchedSeries.length;
    console.log("Nombre de series regardées");
    console.log(myWatchedSeriesLengthdont);
    
    //Créez une variable nommée myWatchedSeriesSentence, qui est égale à une phrase décrivant la série que vous avez regardée
    let myWatchedSeriesSentence=myWatchedSeries.join() ;
    console.log(myWatchedSeriesSentence);
    //Console.log une phrase utilisant les deux variables créées ci-dessus
    console.log("I watched " +myWatchedSeriesLengthdont + " series : "+ myWatchedSeriesSentence);

    //Part 2
    console.log("Part 2 : ");

    //Remplacez la série « the big bang theory » par « friends ». Astuce : Vous devrez utiliser l'index de la série « the big bang theory ».
    myWatchedSeries.splice(myWatchedSeries.indexOf("the big bang theory"),1, "friends");
    console.log("Tableau après remplacement par 'friends' ");
    console.log(myWatchedSeries);

    //Ajoutez, à la fin du tableau, le nom d'une autre série que vous avez regardée.
    myWatchedSeries.push("power");
    console.log("Tableau après ajoue de 'power' ");
    console.log(myWatchedSeries);
    //Ajoutez, au début du tableau, le nom de votre série préférée.
    myWatchedSeries.splice(0,0, "games of throne");
    console.log("Tableau après ajoue de  series préféré ");
    console.log(myWatchedSeries);
    //Supprimer la série « miroir noir ».
    myWatchedSeries.splice(myWatchedSeries.indexOf("black mirror"),1);
    console.log("Tableau après suppression de  'miroir noir' ");
    console.log(myWatchedSeries);
    //Console.log la troisième lettre de la série "money heist".
    console.log("3ème lettre de 'money heist' ");
    console.log(myWatchedSeries[1][2]);
    
    //Enfin, console.log le myWatchedSeries , pour voir toutes les modifications que vous avez apportées.
    console.log("Tableaux final ");
    console.log(myWatchedSeries);

//****************************************************
//Exercise 3
    
    console.log("Exercise 3 : ");
    //Stocker une température Celsius dans une variable.
    let temperature= 45;
    let Fahrenheit= (((temperature / 5) * 9) + 32);

    //Convertissez-le en fahrenheit et console.log <temperature>°C is <temperature>°F.
    console.log("Conversion en Fahrenheit ");
    console.log(temperature +" °C " + " is " + Fahrenheit +" °F");

//****************************************************
//Exercise 4
    
    console.log("Exercise 4 : ");

    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction: It will output 55, because 'a' and 'b' are numbers (a=34; b=21)
    // Actual: 55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: It will output 23, because 'a' and 'b' are numbers (a=2; b=21)
    // Actual: 23


    //Quel sera le résultat de a + b dans la première expression ?
    console.log("première expression: a + b = 55");
    //Quel sera le résultat de a + b dans la seconde expression ?
    console.log("deuxième expression: a + b = 21");
    //Quelle est la valeur de c?
    console.log("c is undefined"); 

    //Analysez le code ci-dessous, quel sera le résultat ?
    console.log(3 + 4 + '5');
    // Prediction: It will output 75, because '3' and '4' are numbers  and '5' is string
    // Actual: 75
    console.log("Resultat is 75 "); 

//****************************************************
//Exercise 4
    
    console.log("Exercise 5 : ");

    //Quelle est la sortie de chacune des expressions ci-dessous ?


    typeof(15);
    // Prediction: It will output Number because 15 is number
    // Actual: Number

    typeof(5.5)
    // Prediction: It will output Number because 5.5 is number
    // Actual: Number

    typeof(NaN)
    // Prediction: It will output Number because NaN type is number
    // Actual: Number

    typeof("hello")
    // Prediction: It will output String because 'hello' is String
    // Actual: String

    typeof(true)
    // Prediction: It will output Boolean because 'true' is Boolean
    // Actual: Boolean

    typeof(1 != 2)
    // Prediction: It will output Boolean because '1 != 2' type is Boolean
    // Actual: Boolean

    "hamburger" + "s"
    // Prediction: It will output hamburgers because "hamburger" and "s"  is String
    // Actual: hamburgers

    "hamburgers" - "s"
    // Prediction: It will output NaN because "hamburger" and "s"  is String and we can not apply an arithmetic operation
    // Actual: NaN

    "1" + "3"
    // Prediction: It will output 13 because "1" and "3"  is String 
    // Actual: 13

    "1" - "3"
    // Prediction: It will output -2 because "1" and "3"  can be convert to number 
    // Actual: -2

    "johnny" + 5
    // Prediction: It will output -johnny5 because "johnny" is a string and 5  can be convert to string 
    // Actual: johnny5

    "johnny" - 5
    // Prediction:  It will output NaN because "johnny" is String and  5 is number . we can not apply  an arithmetic operation
    // Actual :NaN

    99 * "hello"
    // Prediction: It will output NaN because "hello" is String and  99 is number . we can not apply  an arithmetic operation
    // Actual: NaN

    1 != 1
    // Prediction: It will output False because 1 is equal 1 
    // Actual: False

    1 == "1"
    // Prediction:  It will output True because 1 is number and "1" can be convert to number. In additionnal, 1 equal 1 
    // Actual: True

    1 === "1"
    // Prediction:  It will output False because  the type of 1 is number and the type of "1" is string 
    // Actual: False



    //Exercise 4
    
    console.log("Exercise 6 : ");
    //Quelle est la sortie de chacune des expressions ci-dessous ?


    5 + "34"
    // Prediction:  It will output 539 because 5 is number and "34" is string
    // Actual: 539

    5 - "4"
    // Prediction: It will output 1 because 5 is number and "4"  can be convert to number 
    // Actual:

    10 % 5
    // Prediction: It will output 0 because the rest of the integer division between 10 and 5 is 0 
    // Actual: 0

    5 % 10
    // Prediction: It will output 5 because the rest of the integer division between 5 and 10 is 5 
    // Actual:

    "Java" + "Script"
    // Prediction: It will output JavaScript because "Java" and "Script"  is String 
    // Actual: JavaScript

    " " + " "
    // Prediction: It will output " " because "it is a concatenation of " "
    // Actual: " "

    " " + 0
    // Prediction: It will output 0 because "it is a concatenation of " " and 0
    // Actual: 0

    true + true
    // Prediction:  It will output 2 because true is equal 1
    // Actual: 2

    true + false
    // Prediction:  It will output 1 because true is equal 1 and false equal 0
    // Actual: 1

    false + true
    // Prediction: It will output 1 because true is equal 1 and false equal 0
    // Actual: 1

    false - true
    // Prediction: It will output -1 because true is equal 1 and false equal 0
    // Actual: -1

    console.log(!true)
    // Prediction: It will output false because the  inverse of true is flase
    // Actual: False

    3 - 4
    // Prediction: It will output -1 because 3  and 4 are numbers
    // Actual: -1

    "Bob" - "bill"
   // Prediction: It will output NaN because "Bob" and "bill"  is String and we can not apply an arithmetic operation
   // Actual: NaN
