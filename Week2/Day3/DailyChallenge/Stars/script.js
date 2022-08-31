console.log("Daily Challenge : ");
//Write a JavaScript program that recreates the pattern below.
//Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
//Do this Daily Challenge by youself, without looking at the answers on the internet.

for(let i=1;i<=6;i++){
    console.log("*".padStart((i),"*"));
}

//Dexième methode
for(let a=1; a<=6; a++)
{
    for(let j=1; j<=a; j++)
    {
        console.log("*");
    }
    console.log("\n");
}