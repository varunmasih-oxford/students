// Key : value pair
var data = {
    "a":10,
    "b":20,
    "c":30
}
// console.log(data)
console.log(data.b)
data.b = 200
data.b = 200
console.log(data.b)
data.d = 400
console.log(data)

// OBJ AND OBJ
// nested_obj = {
//     "stud_1":{"name":"John","age":20},
//     "stud_2":{"name":"Doe","age":25},
    
// }

// console.log(nested_obj.stud_1.name)
// console.log(nested_obj.stud_1.age)

// OBJ AND Array
// nested_obj = {
//     "stud_1":["John",20],
//     "stud_2":["Doe",25],
    
    
// }

// console.log(nested_obj.stud_1[0])


// array using loop
// var arr = [55,66,33,44,88]

// for(i=0;i<arr.length;i++){
//     // console.log("hey")
//     console.log(arr[i])
    
// }

// obj using loop
var obj = {
    "a":55,
    "b":66,
    "c":33,
    "d":44,
    "e":88
}
console.log(obj)
var len = Object.keys(obj).length
console.log(len)

// for(i=0;i<len;i++){
//     // console.log("hey")
//     console.log(Object.keys(obj)[i])
//     console.log(Object.values(obj)[i])
//     console.log(Object.entries(obj))
    
// }

// console.log(Object.entries(obj)[0])
// console.log(Object.entries(obj)[0][1])

