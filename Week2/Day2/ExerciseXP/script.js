//Exercise 1
    console.log("Exercise 1 : ");
    //Create 2 variables, x and y. Each of them should have a different numeric value.
    let x=5;
    let y=2;
    //Write an if/else statement that checks which number is bigger.
    if(x>y){
        console.log("x est plus grand");
    }
    else if(x<y){
        console.log("y est plus grand");
    }
    


//****************************************************
//Exercise 2
    console.log("Exercise 2 : ");
    
    //Create a variable called newDog where it’s value is “Chihuahua”.
    let newDog="Chihuahua";
    //Check and display how many letters are in newDog.
    console.log("Taille : "+ newDog.length)
    //Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
    console.log("Majiscule : "+ newDog.toUpperCase())
    console.log("Miniscule : "+ newDog.toLowerCase())
    //Check if the variable newDog is equal to “Chihuahua”
    //if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
    //else, console.log ‘I dont care, I prefer cats’
    if(newDog == "Chihuahua"){
        console.log("I love Chihuahuas, it’s my favorite dog breed");
    }
    else if(x<y){
        console.log("I dont care, I prefer cats");
    }

//****************************************************
//Exercise 3
    console.log("Exercise 3 : ");
    
   
    //Prompt the user for a number and save it to a variable.
    let num=Number(prompt("Entrer un nombre",0));
    //Check whether the variable is even or odd.
    //If it is even, display: “x is an even number”. Where x is the actual number the user chose.
    //If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
    if(num%2 ==0){
        console.log(num +" is an even number");
    }
    else{
        console.log(num +" is an odd number");
    }
    

//****************************************************
//Exercise 4
    console.log("Exercise 4 : ");
    let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
    //Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
    //If there is no users (the users array is empty), console.log “no one is online”.
    //If there is 1 user, console.log “<name_user> is online”.
    //If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
    //If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
    //For example, if there are 5 users, it should display:

    if(users.length ==0){
        console.log(" no one is online");
    }
    else if(users.length ==1){
        console.log(users[0] +" is online");
    }
    else if(users.length ==2){
        console.log(users[0] + " and "+users[1]  +" are online");
    }
    else if(users.length >2){
        console.log(users[0] + " , "+users[1]  + " and " +(users.length-2) +" are online");
    }