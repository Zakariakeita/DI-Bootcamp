let nombre;
function number(num){
   
    nombre=document.getElementById("myInput").textContent;
    document.getElementById("myInput").innerHTML= (nombre.toString().concat(Number(num)));
  
}


function operator(operator){
    nombre=document.getElementById("myInput").textContent;
    switch(operator)
    {
        case "*": if(nombre.toString().charAt(nombre.length-1) =="*" || nombre.toString().charAt(nombre.length-1) =="-" || nombre.toString().charAt(nombre.length-1) =="+" ||nombre.toString().charAt(nombre.length-1) =="/" )
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().substring(0,nombre.length-1) + "*");break;

                    }
                    else
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().concat("*"));break;

                    }
        case "+":if(nombre.toString().charAt(nombre.length-1) =="*" || nombre.toString().charAt(nombre.length-1) =="-" || nombre.toString().charAt(nombre.length-1) =="+" ||nombre.toString().charAt(nombre.length-1) =="/" )
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().substring(0,nombre.length-1) + "+");break;

                    }
                    else
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().concat("+"));break;

                    }
        case "-":if(nombre.toString().charAt(nombre.length-1) =="*" || nombre.toString().charAt(nombre.length-1) =="-" || nombre.toString().charAt(nombre.length-1) =="+" ||nombre.toString().charAt(nombre.length-1) =="/" )
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().substring(0,nombre.length-1) + "-");break;

                    }
                    else
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().concat("-"));break;

                    }
        case "/":if(nombre.toString().charAt(nombre.length-1) =="*" || nombre.toString().charAt(nombre.length-1) =="-" || nombre.toString().charAt(nombre.length-1) =="+" ||nombre.toString().charAt(nombre.length-1) =="/" )
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().substring(0,nombre.length-1) + "/");break;

                    }
                    else
                    {
                        document.getElementById("myInput").innerHTML=(nombre.toString().concat("/"));break;

                    }
    }
}

function equal(){
    document.getElementById("myInput").innerHTML=eval(document.getElementById("myInput").textContent.toString());
}

function effacerOne()
{
    nombre=document.getElementById("myInput").textContent.toString();
    document.getElementById("myInput").innerHTML=(nombre.substring(0,nombre.length-1)); 
}
function effacerAll()
{
    document.getElementById("myInput").innerHTML=" ";    
}