//Exercise 1
    console.log("Exercise 1 : ");
    //You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.
    //Create two objects, each object should hold a person’s details. Here are the details:
    //Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person
   
    let personne1= {
        FullName: "Sanou Ali", Mass:70, Height:1.75, IMC: function (){return this.Mass/(this.Height**2);} }
    
    let personne2= {
        FullName: "Traore Madou", Mass:90, Height:1.95 , IMC:function (){return this.Mass/(this.Height**2);} }

    console.log(personne1.FullName + " , IMC: "+personne1.IMC() );
    console.log(personne2.FullName + " , IMC: "+personne2.IMC() );
   
    //Outside of the objects, create a JS function that compares the BMI of both objects.
    //Display the name of the person who has the largest BMI.
    function compareIMC(a,b){
        if(a.IMC() > b.IMC()){
            console.log("person who has the largest BMI " + a.FullName);
        }
        else if(a.IMC() < b.IMC())
        {
            console.log("person who has the largest BMI " + b.FullName);
        }
    }
    
    compareIMC(personne1,personne2);
//****************************************************

//Exercise 2
    console.log("Exercise 2 : ");
    
    function findAvg(gradesList){
        let sum=0;
        
        for(let i=0;i<gradesList.length; i++){
            sum+=gradesList[i];
        }
        let moy=sum/gradesList.length;
        if(moy>65){
            console.log("La moyenne est " + moy +", Vous avez reussi ");
        }
        else if (moy<65){
            console.log("La moyenne est " + moy +", Vous avez échoué ");
        }
    }
    let tableau=[17,17,19,10,15,19,18,17,12];
    findAvg(tableau);

     //Partie bonnus
    function MoyenneBonus(gradesList){
        let sum=0;
        
        for(let i=0;i<gradesList.length; i++){
            sum+=gradesList[i];
        }
        let moy=sum/gradesList.length;
        console.log("La moyenne est " + moy);
        return moy;
    }

    function findAvgBonus(gradesList){
        
        let moy=MoyenneBonus(gradesList);
       
        if(moy>65){
            console.log("Vous avez reussi ");
        }
        else if (moy<65){
            console.log("Vous avez échoué ");
        }
    }
    findAvgBonus(tableau);