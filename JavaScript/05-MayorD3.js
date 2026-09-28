const a = 1;
const b = 1;
const c = 1;
function MayorD3(a,b,c){

    if (c > a && c > b){
        return "C es mayor"
    }

    if (a > b){
        if (a > c){
            return "A es mayor"
        }else{
            return "A y C empatan por mayor"
        }
    }else if(a == b){
        if (a > c)
            return "A y B empatan por mayor"
        else{
            return "Todos los numeros son iguales"
        }
    }else{
         if (b > c){
            return "B es mayor"
        }else{
            return "B y C empatan por mayor"
        }
    }
}

console.log(MayorD3(a,b,c))
