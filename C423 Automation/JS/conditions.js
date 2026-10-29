// conditions

var age = prompt("enter age :") 

// control flow

// if(age > 18){
//     alert("welcome adult")
// }

// if(age > 18){
//     alert("welcome adult")
// }else{
//     alert("Oops..! can not proceed.")
// }

// 0-12 child
// 13-19 teen
// 19-45 young
// 45-70 adult
// 70-120 old

if(age > 0 && age <= 12 ){
    alert("welcome Child")
}else if(age > 12 && age <= 19 ){
    alert("welcome teen")
}else if(age > 19 && age <= 45 ){
    alert("welcome young")
}else if(age > 45 && age <= 70 ){
    alert("welcome adult")
}else if(age > 70 && age <= 120 ){
    alert("welcome old")
}else{
    alert("Oops..! can not proceed.")
}