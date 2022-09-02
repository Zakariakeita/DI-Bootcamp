function playTheGame(){
    
    if (confirm("would like to play the game") == false) 
    {
         alert("No problem, Goodbye");
    } 
    else 
    {
       let val=prompt("Enter a number between 0 and 10");
       if( isNaN(Number(val)))
       {
            alert("Sorry Not a number, Goodbye");
       }
       else if(Number(val)<0 || Number(val)>10)
       {
            alert("Sorry it’s not a good number, Goodbye");
       }
       else
       {
            computerNumber=Math.floor(Math.random() * (10-1));
            alert(computerNumber);
            let i=0;
            
            function compareNumbers(userNumber,computerNumber)
            {
                if( userNumber == computerNumber)
                {
                        alert("WINNER");
                        return true;
                }
                else
                {   
                    if( i<3)
                    {
                        while((userNumber != computerNumber) && (i<3))
                        {
                            
                            if( userNumber > computerNumber)
                            {
                                userNumber=Number(prompt("Your number is bigger then the computer’s, guess again"));
                                i++;
                                compareNumbers(userNumber,computerNumber);
                            }
                            else if( userNumber < computerNumber)
                            {
                                userNumber=Number(prompt("Your number is smaller then the computer’s, guess again"));
                                i++;
                                compareNumbers(userNumber,computerNumber);
                            }
                            break;
                        }
                    }
                    else
                    {
                        alert("out of chances");
                    }
                }
            }
            compareNumbers(Number(val),computerNumber);
       } 
    }
}