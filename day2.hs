import Data.List

-- Just like words, but with a string of integers instead of words.
nums:: String -> [Int]
nums s = sort $ map (\x->read x :: Int) $ words s

minMax:: [Int] -> (Int, Int) -> (Int, Int)
minMax (x:xs) (min, max)
  | x < min = minMax xs (x, max)
  | x > max = minMax xs (min, x)
  | x == min && x == max = minMax xs (x,x)
  | otherwise = minMax xs (min,max)
minMax [] (min,max) = (min,max)

minMax':: [Int] -> (Int, Int)
minMax' xs = (head xs, last xs)

diffMinMax:: (Int,Int) -> Int
diffMinMax (a,b) = abs (a-b)

pairWise':: Int -> [Int] -> [(Int,Int)]
pairWise' a (x:xs) = (a,x):(pairWise' a xs)
pairWise' a _      = []

pairWise:: [Int] -> [(Int,Int)]
pairWise (x:xs) = (pairWise' x xs)++(pairWise xs)
pairWise []     = []

main =
  do
    fileData <- readFile "inputs/day2.input"
    putStrLn "Part One:"
    putStrLn $ show $ sum $ map (diffMinMax . minMax') (map nums $ lines fileData) -- array of [Int]'s

    putStrLn "part Two:"
    -- 1. Make a matrix of [[row1], [row2], ...]
    -- 2. Map each [rowN]
    -- 2.1 Filter each [rowN] for pairs that don't divide.
    putStrLn $ show $ sum $ (map ((\(x,y) -> (quot y x)) . head . filter (\(x,y) -> rem y x == 0) . pairWise) (map nums $ lines fileData))
 --   return $ show numbers

--return $ show $ diffMinMax $ minMax row (head row, last row)



-- map nums $ lines "hey you\nthere here"
