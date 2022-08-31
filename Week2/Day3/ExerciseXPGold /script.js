//Exercise 1
    console.log("Exercise 1 : ");
    //Loop through the array above and determine whether or not each number is divisible by three.
    //Each time you loop console.log true or false.
    let numbers = [123, 8409, 100053, 333333333, 7]
    for(let i in numbers){
        if(i%3==0){
            console.log("True");
        }
        else{
            console.log("False");
        }
    }
    

//****************************************************
//Exercise 2
    
    console.log("Exercise 2 : ");
    let guestList = {
        randy: "Germany",
        karla: "France",
        wendy: "Japan",
        norman: "England",
        sam: "Argentina"
      }

      //Given the object above where the key is the student’s name and the value is the country they are from.

      //Prompt the student for their name.
      let nom=prompt("Entrer le nom:");
      //If the name is in the object, console.log the name of the student and the country they come from.
      //For example: "Hi! I'm [name], and I'm from [country]."
      //Hint: You don’t need to use a for loop, just look up the statement if ... in
      //If the name is not in the object, console.log: "Hi! I'm a guest."
      if(nom in guestList){
         console.log(" Hi! I'm " + nom +" , and I'm from "+ guestList[nom])
      }
      else{
        console.log(" Hi! I'm a guest");
     }
    
//****************************************************
//Exercise 3
    
    console.log("Exercise 3 : ");

    let age = [20,5,12,43,98,55];
    //Console.log the sum of all the numbers in the age array.
    let sum=0;
    for(let i=0; i<age.length;i++){
        sum+=age[i];
     }
    console.log(" Sum =" + sum);

    //Console.log the highest age in the array.
    let temp=age[0];
    for(let i=0; i<age.length;i++){
        if(temp <age[i]){
            temp=age[i];
         }
     }
    console.log(" Plus grand valeur =" + temp);

    
    