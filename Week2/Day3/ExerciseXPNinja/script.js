//Exercise 1
    console.log("Exercise 1 : ");
   
    let date1=1990;
    let date2=2005;
    if((2022 - date2)>(parseInt((2022-date1)/2))) {
        console.log("date à laquelle le plus jeune aura la moitié du plus agé: ");
        console.log((date2-((2022 - date2)- (parseInt((2022-date1)/2)))));
     }
     else if((2022 - date2)<(parseInt((2022-date1)/2))){
        console.log("date à laquelle le plus jeune aura la moitié du plus agé: ");
        console.log((date2+(parseInt((2022-date1)/2))-(2022 - date2)));
     }
   
//****************************************************
//Exercise 2
console.log(typeof("1"));
    console.log("Exercise 2 : ");
    //Part 1
    let post=prompt("Entrer code postal :");
    if(post.length==5 && post.length==post.trim().length)
    {
        if( Number(post))
        {
            console.log("Succès "); 
        }
    
        else
        {
            console.log("Erreur"); 
        }   
    }    
    else
    {
        console.log("Erreur"); 
    }
   

//****************************************************
//Exercise 3
    
    console.log("Exercise 3 : ");
     let mot=prompt("Entrer un mot :");
     console.log(mot.replace(/[aeiou]/gi, ''));
     mot=mot.replace(/[a]/g,1);
     mot=mot.replace(/[e]/g,2);    
     mot=mot.replace(/[i]/g,3); 
     mot=mot.replace(/[o]/g,4);
     mot=mot.replace(/[u]/g,5);    
     console.log(mot);
    