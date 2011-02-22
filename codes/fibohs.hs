--module Fibo where
import System.Environment

import System.Exit


--fibo :: Int -> Int 
fibo 1 = 1
fibo 0 = 0
fibo i = fibo (i-1) + fibo(i-2)



interpret :: String -> String
interpret s = "fibo " ++((words s)!!0)++ ": " ++ show (fibo (read ((words s)!!0)::Int)) 


--module Main where






main = getArgs >>= parse  


parse ["-h"] = usage   >> exit
parse ["-v"] = version >> exit
parse [fs]     = putStrLn (interpret fs)

usage   = putStrLn "Usage: fibohs [-h] n"
version = putStrLn "Haskell fibohs 0.1"
exit    = exitWith ExitSuccess
die     = exitWith (ExitFailure 1)

















