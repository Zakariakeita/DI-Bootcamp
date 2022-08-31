console.log("Daily Challenge : ");
    const numbers = [5,0,9,1,7,4,2,6,3,8];
    //Using the .toString() method convert the array to a string.
    let num1=numbers.toString();
    console.log(num1);

    //Using the .join()method convert the array to a string. Try passing different values into the join.
    //Eg .join(“+”), .join(” “), .join(“”)
    let num2=numbers.join(",");
    console.log(num2);
    let num3=numbers.join("+");
    console.log(num3);
    let num4=numbers.join("");
    console.log(num4);
    let num5=numbers.join(" ");
    console.log(num5);
    //Bonus : To do this Bonus look up how to work with nested for loops
    //Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
    //The output should be: [9,8,7,6,5,4,3,2,1,0]
    //Hint: The algorithm is called “Bubble Sort”
    //Use a temporary variable to swap values in the array.
    //Use 2 “nested” for loops (Nested means one inside the other).
    //Add comments and console.log the result for each step, this will help you understand.
    //Requirement: Don’t copy paste solutions from Google

     
    for (let i = 0; i <numbers.length; i++) 
    { 
          for (let j = 0; j < (numbers.length - i - 1); j++) 
          { 
                if(numbers[j] < numbers[j+1]) 
                {
                    let temp = numbers[j]; 
                    numbers[j] = numbers[j+1]; 
                    numbers[j+1] = temp; 
                 }
        }     
        console.log(numbers);   
    }
    
    console.log("A près trie : " +numbers);  