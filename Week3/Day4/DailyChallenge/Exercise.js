// Todo list
let listTasks = [];
let formulaire,div,contenu,p,check,label;
let form=document.body.firstElementChild.nextElementSibling;
let valeur;
console.log(form);
function addTask(){
    document.getElementById("add").addEventListener("click",function(event){
        valeur=document.getElementById("text").value;
        if(valeur==""){
        alert("hello it is  null");
        }else{
            alert("it is not null");
            listTasks=valeur;
            console.log(listTasks);
            //atteinte du formulaire
            formulaire=document.body.firstElementChild.nextElementSibling;
            //atteinte du div en siblant le prochain element a laide du formualaire
            div= formulaire.nextElementSibling;
          //creation dun nouveau contenu avec la nouvelle tache et stocker dans contnu
            contenu= document.createTextNode(listTasks);
          //creation dun paragraph p et stocker dans la variable p
            p=document.createElement("p");
            //creation du font icone de font aweson
            var font=document.createElement("i");
            font.setAttribute("class","fa-sharp fa-solid fa-xmark");
            //ajout du font dans le paragraph
            p.appendChild(font);
            //creation dun ckeckbox par tache
            check=document.createElement("input");
            check.type='checkbox';
            check.id='choix';
            check.name='choix';
            label=document.createElement("label");
            label.htmlFor=contenu.textContent;
            //ajout du checkbox dans le paragraph 
            p.appendChild(check);
            //ajout du label dans le checkbox
            check.appendChild(label);
          //ajout du contenu du tableau dans la variable p,le paragraphe
            p.appendChild(contenu);
          //ajout du paragraphe dans le div
            div.appendChild(p);


        }
        event.preventDefault();
    });
    
};
addTask();