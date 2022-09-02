console.log("Daily Challenge : ");
let phrase=prompt("Enter your several word");
phrase=phrase.split(",");
console.log(phrase);
let max=0;
for(mot of phrase){
    if(max<mot.length)
    {
        max=mot.length;
    }
}

for(let i=0;i<phrase.length;i++)
{
    
    if(i==0) 
    {
        console.log("*".padStart((max+4),"*"));
    }
        console.log("* " +phrase[i].concat("".padStart(((max+4)-2)-(2+phrase[i].length)), " ") +"*");
    if(i==phrase.length-1)
    {
        console.log("*".padStart((max+4),"*"));
    }
}