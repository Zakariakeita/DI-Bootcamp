console.log("Daily Challenge : ");
let num;
do
{
     num=Number(prompt(" Enter number to begin counting down bottles"));
}while(isNaN(Number(num)));

alert("We start the song at " + Number(num) +" bottles");
let i=1;
num=Number(num);
do
{
    if((num-i) >=0)
    {
        if(i==1)
        {
        alert("Take _" + i +"_ down, pass it around \n" +"we have now "+ (num-i) +" bottles");
        num=(num-i);
        i+=1;
        }
        else
        {
            alert("then, Take _" + i +"_ down, pass it around \n" +"we have now "+ (num-i) +" bottles");
            num=(num-i);
            i+=1;
        }
    }
    else
    {
        alert("then, Take _" + i +"_ down, pass it around \n" +"we have now "+ 0 +" bottles");
        break;
    }
}while(num > 0);

