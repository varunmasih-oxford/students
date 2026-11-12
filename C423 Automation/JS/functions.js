// function 
// buit-in functions - alert(), prompt(), confirm()
// user-defined functions - abc(), xyz(), printNumbers()
// syntax of function
// types of function - 
// no arguments and no return value

// ie:
// function abc(){
//     document.write("<h1>Hey</h1>")
// }
// abc()
// abc()
// abc()
// abc()
// abc()
// abc()
// abc()
// abc()
// abc()

// arguments and no return value

// function xyz(x){
//     document.write(`<h1>Hey ${x}</h1>`)
// }

// xyz("Alice")
// xyz("Bob")
// xyz("Charlie")
// xyz("David")
// xyz("Eve")
// xyz("Frank")
// xyz("Grace")
// xyz("Henry")
// xyz("Ivy")


// no arguments and return value
// ie:
// function abc(){
//     var txt = "Hey"
//     return txt
// }



// var y = abc()

// arguments and return value
function abc(x){
    var txt = `Hey ${x}`
    return txt
}



document.write(abc(prompt("enter your name : ")))

// function function_name(parameters){
//     // code block    
// }
// function calling - function_name(arguments)


// for(var a = 1; a <= 10; a++){
//     if(a == 8){
//         continue    
//     }
//     document.write(`${a}<br>`)
// }

// for(var a = 11; a <= 20; a++){
//     if(a == 15){
//         continue    
//     }
//     document.write(`${a}<br>`)
// }

// for(var a = 21; a <= 30; a++){
//     if(a == 25){
//         continue    
//     }
//     document.write(`${a}<br>`)
// }

// function - reuseable code blocks

// function mlt(param1, param2){
//     var mlt_value = param1 * param2        
//     alert(`the multiplication of ${param1} and ${param2} is ${mlt_value}`)
// }
// mlt(50,100) // function calling
// using prompt() to get user input

// var x = Number(prompt("enter first number : "))
// var y = Number(prompt("enter second number : "))
// mlt(x,y) // function calling



// function printNumbers(start, end, skip){
    
//     for(var a = start; a <= end; a++){
//         if(a == skip){
//             continue
//         }
//         document.write(`${a}<br>`)
//     }

// }

// printNumbers(100,105,103)
// printNumbers(200,205,203)
// printNumbers(300,305,303)




