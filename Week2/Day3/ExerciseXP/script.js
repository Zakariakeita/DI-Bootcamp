//Exercise 1
    console.log("Exercise 1 : ");
    console.log("Part 1 : ");
    let people = ["Greg", "Mary", "Devon", "James"];
    //Write code to remove “Greg” from the people array.
    people.shift();
    //Write code to replace “James” to “Jason”.
    people.splice(2,1,"Jason");
    //Write code to add your name to the end of the people array.
    people.push("Keita");
    //Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
    console.log(people.indexOf("Mary"));
    //Write code to make a copy of the people array using the slice method.
    //The copy should NOT include “Mary” or your name.
    //Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
    //Hint: Check out the documentation for the slice method
    let people2=people.slice(0,people.indexOf("Keita"));
    console.log(people2);
    
    //Write code that gives the index of “Foo”. Why does it return -1 ?
    console.log(people.indexOf("Foo"))
    //Create a variable called last which value is the last element of the array.
    //Hint: What is the relationship between the index of the last element in the array and the length of the array?
    let last=people[(people.length-1)];
    console.log(last);

    console.log("Part 2 : ");
    //Using a loop, iterate through the people array and console.log each person.
    for(let i in people){

           console.log(people[i]);
    }
    //Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
    //Hint: take a look at the break statement in the lesson.
    for(let i in people){
        console.log(people[i]);
        if(people[i] =="Jason"){

            break;
     }
        
 }


//****************************************************
//Exercise 2
    console.log("Exercise 2 : ");
    
    //Create an array called colors where the value is a list of your five favorite colors.
    let colors=["red","orange","blue","green","yellow"];
    //Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
    for(let i in colors){

        console.log("My #" + ((parseInt(i)+1)) + " choice is " +colors[i]);
    }
    //Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
    //Hint : create an array of suffixes to do the Bonus
    let suf=["1st","2nd","3rd","4th","5th"]
    for(let i in colors){

        console.log("My " + (suf[i]) + " choice is " +colors[i]);
    }

//****************************************************
//Exercise 3
    console.log("Exercise 3 : ");
    
    //Prompt the user for a number.
    //Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
    let num=prompt("Entrer un nombre",0);
    typeof(num)
    Number(num);
     //While the number is smaller than 10 continue asking the user for a new number.
    //Tip : Which while loop is more relevant for this situation?

    while(num <10)
    {
        num=Number(prompt("Re-entrer un nombre",0));
    }
   
    

//****************************************************
//Exercise 4
    console.log("Exercise 4 : ");
    //Copy and paste the above object to your Javascript file.
    let building = {
        numberOfFloors : 4,
        numberOfAptByFloor : {
            firstFloor : 3,
            secondFloor : 4,
            thirdFloor : 9,
            fourthFloor : 2,
        },
        nameOfTenants : ["Sarah", "Dan", "David"],
        numberOfRoomsAndRent:  {
            sarah: [3, 990],
            dan :  [4, 1000],
            david : [1, 500],
        },
    }
    
    //Console.log the number of floors in the building.
    console.log("number of floors "+ building.numberOfFloors);
    //Console.log how many apartments are on the floors 1 and 3.
    
    console.log("apartments in floors 1 : "+ building.numberOfAptByFloor.firstFloor);
    console.log("apartments in floors 3 : "+building.numberOfAptByFloor.thirdFloor);
    //Console.log the name of the second tenant and the number of rooms he has in his apartment.
    console.log("name of the second tenant : "+ building.nameOfTenants[1]);
    console.log("number of rooms of the second tenant : "+ building.numberOfRoomsAndRent.dan[0]);
    //Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
    if(building.numberOfRoomsAndRent.david[1] +building.numberOfRoomsAndRent.sarah[1] >building.numberOfRoomsAndRent.dan[1]) {
        building.numberOfRoomsAndRent.dan[1]+=1200;
        console.log("Dan’s rent : "+ building.numberOfRoomsAndRent.dan[1]);
    }

//****************************************************
//Exercise 5
    console.log("Exercise 5 : ");
    //Create an object called family with a few key value pairs.
    let family= {name:"Sanou", number:5, child:3,childName: ["Sarah", "Dan", "David"]}

    //Using a for in loop, console.log the keys of the object.
    console.log("clé: ");
    for(let i in family){

        console.log(i);
    }
    //Using a for in loop, console.log the values of the object.
    console.log("value: ");
    for(let i in family){

        console.log(family[i]);
    }

//****************************************************
//Exercise 6
    console.log("Exercise 6 : ");

    let details = {
        my: 'name',
        is: 'Rudolf',
        the: 'raindeer'
      }
    //Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
    for(let i in details){
        
        console.log(i + " " + details[i]);
        
    }

//****************************************************
//Exercise 7
    console.log("Exercise 7 : ");


    let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
    //A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
    //Hint: a string is an array of letters
    //Console.log the name of their secret society. The output should be “ABJKPS”
    let secret="";
    for(let i=0;i<names.length;i++){
        console.log(names[i][0]);
        secret=secret.concat(names[i][0]);
        
        
    }
    console.log("Nom societé : " +  secret.split("").sort().toString().replace(/[,]/gi, ''));