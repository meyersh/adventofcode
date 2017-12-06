-- Just like words, but with a string of integers instead of words.
nums:: String -> [Int]
nums s = map (\x->read x :: Int) $ words s

minMax:: [Int] -> (Int, Int) -> (Int, Int)
minMax (x:xs) (min, max)
  | x < min = minMax xs (x, max)
  | x > max = minMax xs (min, x)
  | x == min && x == max = minMax xs (x,x)
  | otherwise = minMax xs (min,max)
minMax [] (min,max) = (min,max)

minMax':: [Int] -> (Int, Int)
minMax' (x:xs) = minMax (x:xs) (x,x)

diffMinMax:: (Int,Int) -> Int
diffMinMax (a,b) = abs (a-b)

main =
  do
    fileData <- readFile "inputs/day2.input"
    putStrLn "Part One"
    putStrLn $ show $ sum $ map (diffMinMax . minMax') (map nums $ lines fileData) -- array of [Int]'s
 --   return $ show numbers

--return $ show $ diffMinMax $ minMax row (head row, last row)



-- map nums $ lines "hey you\nthere here"
