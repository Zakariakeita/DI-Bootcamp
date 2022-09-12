var main=document.body.firstElementChild.nextElementSibling;
function div(){
    for(let i=0;i<=480;i++){
        
       var div= document.createElement("div");
       main.appendChild(div);
    //    if(i==25 || i==50 || i==75){
        var br=document.createElement("br");
        div.appendChild(br);
       }

    // }
  
}
div();