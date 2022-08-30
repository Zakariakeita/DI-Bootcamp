//Exercise 1
    console.log("Exercise 1 : ");
   
    let sentence = ["my","favorite","color","is","blue"];
    //Write some simple Javascript code that will join all the items in the array above, and console.log the result.
    console.log("Affichage resultat ");
    console.log(sentence.join());

//****************************************************
//Exercise 2
    
    console.log("Exercise 2 : ");

    //Create 2 variables. The values should be strings. For example:
    let str1 = "mix";
    let str2 = "pod";
    
    //Slice out and swap the first 2 characters of the two strings from part 1.
    let str3 = str2;
    str2=str2.replace(str2[0],str1[0]);
    str1=str1.replace(str1[0],str3[0]);
    console.log("Chaine 'mix': ");
    console.log(str1);
    console.log("Chaine 'pod': ");
    console.log(str2);
    //Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
    let str4= str1.concat(" ", str2 ) ;
    console.log("Affichage resultat ");
    console.log(str4);

    //Finally console.log the new concatenated string.
    console.log("Affichage Final ");
    console.log(str4);

//****************************************************
//Exercise 3
    
    console.log("Exercise 3 : ");
        
    //Make a Calculator. Follow the instructions:

    //Prompt the user for the first number.
    //Store the first number in a variable called num1.
    //Hint : console.log the type of the variable num1. What should you do to convert it to a number ?
    let num1=Number(prompt("Enter the first num :", 0));
    console.log(typeof(num1) );
    console.log(num1);
  
    //Prompt the user for the second number.
    //Store the second number in a variable called num2.
    let num2=Number(prompt("Enter the second num :", 0));
    console.log(typeof(num2) );
    console.log(num2);

    //Create an Alert where the value is the SUM of num1 and num2.
    alert(num1 +" + " +num2 +" = " + (num1+num2))
    //BONUS: Make a program that can subtract, multiply, and also divide!
    alert(num1 +" - " +num2 +" = " + (num1-num2))
    alert(num1 +" * " +num2 +" = " + (num1*num2))
    alert(num1 +" / " +num2 +" = " + (num1/num2))