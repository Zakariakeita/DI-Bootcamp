//Exercise 1
    console.log("Exercise 1 : ");
    let num= Math.floor(Math.random() * (100-1) +1);
    for(let i=0; i<=num;i++)
    {
       if(i%2==0){
        console.log(i);
        }
    }
   
    
//****************************************************

//Exercise 2
    console.log("Exercise 2 : ");
    function capitalize(mot) {
        mot=mot.toLowerCase();
        let tab=[];
        for (let i = 0; i < mot.length; i++) {
            if (i%2==0) {
                mot=mot.replace(mot[i],mot[i].toUpperCase());
            }
        }
        tab.push(mot);
        mot=mot.toLowerCase();
        for (let i = 0; i < mot.length; i++) {
            if (!(i%2==0)) {
                mot=mot.replace(mot[i],mot[i].toUpperCase());
            }
        }
        tab.push(mot);

        console.log(tab);
    }
    capitalize("abcdef");

//****************************************************

//Exercise 3
    console.log("Exercise 3 : ");
    function palindrome(mot) {

    for (let i = 0; i < (mot.length/2); i++) {

        if (mot[i] != mot[(mot.length - 1) - i]) {
            return (mot +" is not a palindrome");
        }
    }
    return (mot +" is  a palindrome");
    }

    console.log(palindrome("ahd"));

//****************************************************

//Exercise 4
    console.log("Exercise 4 : ");
    function biggestNumberInArray(arrayNumber)
    {
        let j=0;
        while(isNaN(Number(arrayNumber[j])) && j<arrayNumber.length-1 )
        {  
            j++;
        }
        if(isNaN(Number(arrayNumber[j])) || arrayNumber.length==0)
        {  
            return 0;
        }
        else
        {
            let temp=arrayNumber[j];
            
           for (let i = 0; i < arrayNumber.length; i++) 
            {
                if(typeof(arrayNumber[i]) == 'string')
                {
                    continue;
                }
    
                if(temp<arrayNumber[i] )
                {
                    temp=arrayNumber[i];
                }
                
            }
           return temp;
        }
        
    }
    console.log(biggestNumberInArray([-1,0,3,100, 99, 2, 99]));
    console.log(biggestNumberInArray(['a', 3, 4, 2]));
    console.log(biggestNumberInArray([]));

//****************************************************

//Exercise 5
    console.log("Exercise 5 : ");
    function uniqueElement(tab) {
        let tab2 = [];
        for(let i = 0; i < tab.length; i++) {
            if(!tab2.includes(tab[i])) {
                tab2.push(tab[i]);
            }
        }
        return tab2; 
    }
        console.log(uniqueElement([1,2,3,3,3,3,4,5]));
        console.log(uniqueElement([1,2,3,3,3,3,4,5]));
    