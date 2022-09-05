//Exercise 1
    console.log("Hangman");
    let mot;
    let lettre;
    do
    {
       mot=prompt("Enter a word");
    }while(mot.length<8);
    //let mot2=mot.substring(0,)
    //console.log("".padStart(mot.length,"*"));
    
   /* do
    {
       lettre=prompt("Enter a letter");
       if(lettre in mot)
       {
            console.log("".padStart(mot.length,"*"));
             mot=prompt("Enter a word");
        }

    }while(mot.length<8)*/

    let code=[];
    for(let i=0;i<mot.length;i++)
    {
        code[i]="*"
    }
    console.log(mot);

    let taille=mot.length

    while(taille>0)
    {
       let letter=prompt("Enter a letter");
       
        if(letter.length !=1)
       {
        console.log("you have alreay chosen this");
       
        }
        else if(mot.includes(letter))
       {
            break;
        }
    }