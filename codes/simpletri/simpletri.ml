
open Sys;;
open List;;
open Printf;;
open Gc

(*let get_int_from_file inf = *)
(*  let l = ref [] in*)
(*    let ch = open_in inf in*)
(*    try*)
(*     while true do*)
(*       let i = int_of_string (input_line ch) in*)
(*       l := append !l [i]*)
(*     done;[]*)
(*    with End_of_file ->*)
(*     close_in ch;*)
(*     List.rev !l;;*)

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


let simpletria a = 
        let len = Array.length a in
        let min = ref 0 in
        for i = 0 to len-1 do
                min := i ;
                for j = i+1 to len-1 do
                        if a.(j) < a.(!min) then min := j 
                done ;
                if !min != i then 
                        let x = a.(i) in 
                        a.(i) <- a.(!min) ; a.(!min) <- x
        done ;
        a
;;

let ia = Array.of_list (lire_fich Sys.argv.(1)) in 
let sa = simpletria ia in 
let oc = open_out Sys.argv.(2) in 
Array.iter (Printf.fprintf oc "%d\n") sa ;
close_out oc ;;  (* flush and close the channel *) 


(*(*let rec simpletri unsortedlist = match unsortedlist with*)*)
(*(*  | [] -> []*)*)
(*(*  | [a] -> [a]*)*)
(*(*  | head :: tail ->  let (mas,ras) = mini tail head [] in*)*)
(*(*    Gc.compact (); mas:: simpletri ras  ;;*)*)




(*(*let rec mini l c up = match l with *)*)
(*(*  | head :: tail when  head < c ->  mini tail head (append [c] up) *)*)
(*(*  | head :: tail -> mini tail c (append [head] up) *)*)
(*(*  | [] ->     (c,up);;*)*)
(*let rec mini l c up = match l with *)
(*  | [] ->     (c,up)*)
(*  | head :: tail when  head < c ->  mini tail head (c::up) *)
(*  | head :: tail -> mini tail c (head::up);;*)

(*let rec simpletri unsortedlist sl= match unsortedlist with*)
(*  | [] -> sl*)
(*  | [a] -> sl@[a]*)
(*  | head :: tail ->  let (mas,ras) = mini tail head [] in*)
(*  simpletri ras (sl@[mas]) ;;*)

(*let fff a b = a ^ "\n" ^ b ;;*)

(*let rec format_list l = *)
(*  let head::tail = List.map string_of_int l in*)
(*  List.fold_left fff head tail;;*)

(*(*put_str_in_file (format_list (simpletri (get_int_from_file argv.(1)))) argv.(2);;*)*)

(*let oc = open_out  argv.(2) in *)
(*fprintf oc "%s\n" (format_list (simpletri (get_int_from_file argv.(1)) [])); (* write something *)*)
(*close_out oc;;(* flush and close the channel *)*)



