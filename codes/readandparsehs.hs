--module Fibo where
import System.Environment

import System.Exit


--fibo :: Int -> Int 
fibo 1 = 1
fibo 0 = 0
fibo i = fibo (i-1) + fibo(i-2)



interpret :: String -> IO String
interpret s =  return (unlines ( map show ((map (\x-> read x::Int) (lines s)))))

--"fibo " ++((words s)!!0)++ ": " ++ show (fibo (read ((words s)!!0)::Int)) 


--module Main where

--sorted [a] = True
--sorted (a:(b:as)) = if (a<b) then sorted (b:as) else False

mini [] a up = (a,up)
mini (a:as) c up = if a < c then mini as a (c:up) else mini as c (a:up)

simpletri [a] = [a]
simpletri (a:as) = (mas:simpletri ras)
	where 
		(mas,ras) = mini as a []



main = getArgs >>= parse  


parse ["-h"] = usage   >> exit
parse ["-v"] = version >> exit
parse [fi,fo]     =  (readFile fi) >>= interpret  >>= (writeFile fo)




usage   = putStrLn "Usage: simpletrihs [-h] [-v] filenamein filenameout"
version = putStrLn "Haskell simpletrihs 0.1"
exit    = exitWith ExitSuccess
die     = exitWith (ExitFailure 1)

















