
open Sys;;

let rec fibo i = if i <=1 then i else fibo(i-1)+fibo(i-2);;

let valeur =  fibo (int_of_string(argv.(1)));;
let strres =  "fibo "^argv.(1)^": "^(string_of_int valeur) ;;
print_endline strres;;




