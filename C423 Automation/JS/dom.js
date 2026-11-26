//    var x = document.getElementsByTagName("h1")
    //    var x = document.getElementById("a")
    //    var x = document.getElementsByClassName("abc")
    
    //    var x = document.getElementsByClassName("abc")[2]
    //    var x = document.getElementsByClassName("abc")[2].innerText
    //    var x = document.getElementsByClassName("abc")[2].innerHTML
    //    var x = document.getElementsByClassName("abc")[0].attributes
    //    var x = document.getElementsByClassName("abc")[0].getAttribute("id")
    
    // var val = prompt("type:")
    // var x = document.getElementsByClassName("abc")[2].innerText = prompt("type:")
    // console.log(x);
    // alert("Welcome to the JavaScript tutorial!");

    function change_clr(){
        document.getElementsByClassName("abc")[0].setAttribute("class","clr_grey")
    
    }
    function change_clr_blu(){
        document.getElementsByClassName("clr_grey")[0].setAttribute("class","abc")
    
    }