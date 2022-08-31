//Exercise 1
    console.log("Exercise 1 : ");
   
    let mot=prompt("Entrer la langue :");
    mot=mot.toLowerCase();
    switch(mot){
        case "french": console.log("Bonjour"); break;
        case "english": console.log("Hello"); break;
        case "hebrew": console.log("shalom"); break;
        default: console.log("01110011 01101111 01110010 01110010 01111001"); break;
    }

//****************************************************
//Exercise 2
    
    console.log("Exercise 2 : ");

    let note=Number(prompt("Entrer la note :"));
    
    switch(true){
        case note> 90: console.log("A"); break;
        case note>80 && note<=90: console.log("B"); break;
        case note>70 && note<=80: console.log("C"); break;
        case note<70: console.log("D"); break;
        default: console.log("Erreur"); break;
    }

//****************************************************
//Exercise 3
    
    console.log("Exercise 3 : ");
    let verb=prompt("Entrer un verb :");
    switch(true){
        case (verb.length >= 3 && (verb.slice((verb.length)-3)) != "ing"): console.log(verb.concat("ing")); break;
        case (verb.length >= 3 && (verb.slice((verb.length)-3)) == "ing"): console.log(verb.concat("ly")); break;
        case (verb.length < 3): console.log(verb); break;
        default: console.log("Erreur"); break;
    }
        
    