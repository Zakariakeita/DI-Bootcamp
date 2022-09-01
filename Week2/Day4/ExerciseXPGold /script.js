//Exercise 1
    console.log("Exercise 1 : ");
    function isBlank(a){
        if(a =='')
        {
            
            return true;
        }
        else
        {
            return false;
        }
    
    }
    console.log(isBlank(''));
    console.log(isBlank('abc'));
//****************************************************
//Exercise 2
    
    console.log("Exercise 2 : ");
    function abbrevName(a){
        a.toString();
        return (a.slice(0,(a.indexOf(' ')+2)).concat("."));
    }
    console.log(abbrevName("Robin Singh"));
      
//****************************************************
//Exercise 3
    console.log("Exercise 3 : ");
    function swapCase(a){
        a.toString();
        for(let i=0;i<a.length;i++){
            
            if(a[i] == a[i].toLowerCase())
            {
                
                a=a.replace(a[i], a[i].toUpperCase());

                
            }
            else if(a[i] == a[i].toUpperCase())
            {
                a=a.replace(a[i], a[i].toLowerCase());
            }
        }
        return (a);
    }
    console.log(swapCase("The Quick Brown Fox"));

//****************************************************
//Exercise 4
    console.log("Exercise 4 : ");
    function isOmnipresent(tab, nb) {
        for (let i = 0; i < tab.length; i++) {
            if (nb in tab[i]) {
                return true
            }
        }
        return false;
    }
    console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1))
    console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6))
      