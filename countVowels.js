//const str = "javaScript is good programming language";
// vowels = ['a','e','i','o','u'];

// function countVowels(data){
    //     let count = 0;
    
    
    //     data.toLowerCase().split("").forEach((ch)=>{
        //         vowels.includes(ch) && count++;
        //     })
        
        //     console.log(count);
        
        // }
        
        // const numberOfVowels = countVowels(str);

                // OR
        
const str = "javaScript is good programming language";
const string = str.toLowerCase().split("");
let count = 0;
for(let i=0; i < str.length; i++){
    if (string[i]=="a" || string[i]=="e" || string[i]=="i" || string[i]=="o" || string[i]=="u"){
        count = count+1;
    }
}
console.log(count);