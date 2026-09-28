const x = 91;
let primo = true;
for (let i = 2; i <= Math.sqrt(x); i++){
    if (x % i == 0){
        primo = false
        break
    }
}

if (primo){
    console.log("Es primo")
}else{
    console.log("No es primo")
}
