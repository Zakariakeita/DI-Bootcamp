//Exercise 1
    console.log("Exercise 1 : ");
   
    5 >= 1
    // Prediction:  It will output true because 5 is more great than 1 
    // Actual: true
    0 === 1
    // Prediction:  It will output true because 0 and 1 are numbers
    // Actual: true
    4 <= 1
    // Prediction:  It will output false because 4 is more great than 1 
    // Actual: false
    1 != 1
    // Prediction:  It will output false because 1 is equal 1 
    // Actual: false
    "A" > "B"
    // Prediction:  It will output false because in ascii code the value of B is more great than A 
    // Actual: false
    "B" < "C"
    // Prediction:  It will output TRUE because in ascii code the value of C is more great than B 
    // Actual: TRUE
    "a" > "A"
      // Prediction:  It will output TRUE because in ascii code the value of a is more great than A 
    // Actual: TRUE
    "b" < "A"
    // Prediction:  It will output false because in ascii code the value of b is more great than A 
    // Actual: false
    true === false
    // Prediction:  It will output true because true and false are booleans
    // Actual: true
    true != true
    // Prediction:  It will output false because true is equal true 
    // Actual: false

//****************************************************
//Exercise 2
    
    console.log("Exercise 2 : ");

    let val=prompt("Entrer deux nombre separer par une virgule: ");
    let sum= Number(val[0]) + Number(val[2]);
    alert(val +" = "+ sum);

//****************************************************
//Exercise 3
    
    console.log("Exercise 3 : ");
    //Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo"
    let val2=prompt("Entrer une phrase contenant Nemo: ");
    //Find the word “Nemo”
    //Console.log a string as follows: "I found Nemo at [the position of the word Nemo]".
    if(val2.indexOf("Nemo") !=-1) {
       alert("I found Nemo at "+ val2.indexOf("Nemo"));
    }
      //If you can’t find Nemo, console.log “I can’t find Nemo”.
    else{
        alert("I can’t find Nemo");
    }
    
    
//****************************************************
//Exercise 4
    console.log("Exercise 4 : ");
    let nb= Number(prompt("Entrer un nombre: "));
     if(nb <2)
    {
        alert("boum");
    }
    else if(nb >2){
        if((nb%5==0) && (nb%2==0)){
            let maj1=("b".padEnd((nb+1),"o") + "um!")
            alert(maj1.toUpperCase() );
        }
        else if(nb%2==0){
            alert("b".padEnd((nb+1),"o") + "um!" );
        }
        else if(nb%5==0){
            let maj2=("b".padEnd((nb+1),"o") + "um")
            alert(maj2.toUpperCase() );
        }
        else{
            alert("b".padEnd((nb+1),"o") + "um" );
        }
           
    }


    