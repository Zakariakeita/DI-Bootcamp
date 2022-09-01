//Exercise 1
    console.log("Exercise 1 : ");
    console.log("Part 1 : ");
     function infoAboutMe(){
        console.log("Name: Sanou , Age: 17 , Hobbies: ['Football','Reading']");
    }
    infoAboutMe();

    console.log("Part 2 : ");
    function infoAboutPerson(personName,personAge,personFavoriteColor){
        console.log("Your name is "+ personName + " you are "+personAge + " years " + " and your favorite color is "+personFavoriteColor);
    }
    infoAboutPerson("David",45,"Blue");
    infoAboutPerson("Josh",12,"Yellow");
//****************************************************
//Exercise 2
    console.log("Exercise 2 : ");
     function calculateTip()
     {
        let montant=Number(prompt("The amount of the bill",0));
        let tip=0;
        let total=0;
         if( montant<50){
            tip=1.2;
            total= montant*tip;
        }
        else if( montant>=50 && montant<=200  ){
            tip=1.15;
            total= montant*tip;
        }
        else if( montant>200  ){
            tip=1.10;
            total= montant*tip;
        }
        console.log("Tip is :" +tip + " The final bill is : "+ total);
            
    }

    calculateTip();
      
//****************************************************
//Exercise 3
    console.log("Exercise 3 : ");
    
    //Bonnus
    function isDivisible(a){
        let sum=0;
        for(let i=0;i<=500;i++){
            if( i%a==0){
                console.log(i +" is divisible by "+a);
                sum+=i
        
            }
        }
        console.log("Sum of all numbers that are  divisible by "+a +" : "+ sum);
    }
    let num=Number(prompt("Enter the number",0));

    isDivisible(num);

//****************************************************
//Exercise 4
    console.log("Exercise 4 : ");
   
   let stock={ "banana": 6, "apple":0, "pear":12, "orange":32, "blueberry":1};
   let prices={ "banana": 4, "apple":2, "pear":1, "orange":1.5, "blueberry":10};
   shoppingList=["banana","orange","apple"];

   function myBill()
   {
       let sum=0;
        for(let i in shoppingList)
        {
            for(let j in stock)
            {
                if((shoppingList[i] == j) && (stock[j]>=1))
                {
                    sum+=prices[j];
                    //bonnus
                    stock[j]=stock[j]-1;
                       
                }
                 
            }
         }
         return sum;
    }
console.log(myBill());
console.log(stock);
   
//****************************************************
//Exercise 5
    console.log("Exercise 5 : ");

    function changeEnough(itemPrice, amoutOfChange)
   {
       let changeReprentation=[0.25,0.10,0.05,0.01]
       let sum=0;
        for(let i in amoutOfChange)
        {
            sum+=amoutOfChange[i]*changeReprentation[i]
        }
        if(sum>=itemPrice)
        {
            return true;
        }
        else
        {
            return false;
        }
    }    

    console.log(changeEnough(14.11, [2,100,0,0]));
    console.log(changeEnough(0.75, [0,0,20,5]));
    

//****************************************************
//Exercise 6
    console.log("Exercise 6 : ");

    function hotelCost(numNight)
   {
        return numNight*140;
    }    

    function planeRideCost(destination)
   {
    
       destination=destination.toLowerCase().charAt(0).toUpperCase() +destination.slice(1);
       if(destination=="London"){
        return 183;
        }
        else if(destination=="Paris"){
            return 220;
        }
        else{
            return 300;
        }
        
    }    

    function rentalCarCost(numDay)
    {
        
        if(numDay>10){
            return (numDay*40)*0.95;
            }
        else{
                return numDay*40;
            }
        
     }    
    

     function totalVacationCost()
     {  
        let destination=prompt("Enter thier destination : ");
        while( typeof destination != 'string' || destination == "" | destination == " " )
        {
             destination=prompt("Enter against thier destination  ")
        }

        let numDay=prompt("Enter number of day : ");
        while(!Number(numDay))
        {
            numDay=prompt("Enter against number of day  ")
        }

        let numNight=prompt("Enter number of nights: ");
       while(!Number(numNight))
       {
            numNight=prompt("Enter against number of nights: ");
       }

        return (rentalCarCost(numDay)+planeRideCost(destination)+hotelCost(numNight));
         
      }    

      console.log("Total : " +totalVacationCost());

//****************************************************
//Exercise 7
    console.log("Exercise 7 : ");

