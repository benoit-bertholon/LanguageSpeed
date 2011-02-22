
open Sys;;
open List;;
open Printf;;
open Gc

let get_int_from_file inf = 
  let l = ref [] in
    let ch = open_in inf in
    try
     while true do
       let i = int_of_string (input_line ch) in
       l := append !l [i]
     done;[]
    with End_of_file ->
     close_in ch;
     List.rev !l;;


(*let rec simpletri unsortedlist = match unsortedlist with*)
(*  | [] -> []*)
(*  | [a] -> [a]*)
(*  | head :: tail ->  let (mas,ras) = mini tail head [] in*)
(*    Gc.compact (); mas:: simpletri ras  ;;*)




(*let rec mini l c up = match l with *)
(*  | head :: tail when  head < c ->  mini tail head (append [c] up) *)
(*  | head :: tail -> mini tail c (append [head] up) *)
(*  | [] ->     (c,up);;*)
let rec mini l c up = match l with 
  | [] ->     (c,up)
  | head :: tail when  head < c ->  mini tail head (c::up) 
  | head :: tail -> mini tail c (head::up);;

let rec simpletri unsortedlist sl= match unsortedlist with
  | [] -> sl
  | [a] -> sl@[a]
  | head :: tail ->  let (mas,ras) = mini tail head [] in
  simpletri ras (sl@[mas]) ;;

let fff a b = a ^ "\n" ^ b ;;

let rec format_list l = 
  let head::tail = List.map string_of_int l in
  List.fold_left fff head tail;;

(*put_str_in_file (format_list (simpletri (get_int_from_file argv.(1)))) argv.(2);;*)

let oc = open_out  argv.(2) in 
fprintf oc "%s\n" (format_list (simpletri (get_int_from_file argv.(1)) [])); (* write something *)
close_out oc;;(* flush and close the channel *)



