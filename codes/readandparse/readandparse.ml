
open Sys;;
open List;;
open Printf;;
open Gc

let lire_fich fich = 
        let ic = open_in fich in
        let lire_ligne n = try 
                Some (int_of_string (input_line ic))
                with End_of_file -> None 
        in
        let is = Stream.from lire_ligne in
        let rec cons_ acc = try 
                let n = Stream.next is in 
                cons_ (n::acc)
                with Stream.Failure -> acc 
        in
        let l = cons_ [] in
        close_in ic ; 
        l
;;


(*let rec simpletri unsortedlist = match unsortedlist with*)
(*  | [] -> []*)
(*  | [a] -> [a]*)
(*  | head :: tail ->  let (mas,ras) = mini tail head [] in*)
(*    Gc.compact (); mas:: simpletri ras  ;;*)




(*let rec mini l c up = match l with *)
(*  | head :: tail when  head < c ->  mini tail head (append [c] up) *)
(*  | head :: tail -> mini tail c (append [head] up) *)
(*  | [] ->     (c,up);;*)
let fff a b = a ^ "\n" ^ b ;;

let rec format_list l = 
  let head::tail = List.map string_of_int l in
  List.fold_left fff head tail;;

(*put_str_in_file (format_list (simpletri (get_int_from_file argv.(1)))) argv.(2);;*)

let oc = open_out  argv.(2) in 
fprintf oc "%s\n" (format_list (lire_fich  argv.(1))); (* write something *)
close_out oc;;(* flush and close the channel *)



