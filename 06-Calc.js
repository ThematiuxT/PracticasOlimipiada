const a = 3;
const b = 0;
const op = "/";

if (op == "+"){
    console.log(a+b)
}else if (op == "-"){
    console.log(a-b)
}else if (op == "*"){
    console.log(a*b)
}else if (op == "/"){
    if (b == 0){
        console.log("Error: Division entre Zero")
    }else{
        console.log(a/b)
    }
}else {
    console.log("Operacion invalida, elije (+,-,* o /)")
}
