import Data.Char

strToInts:: String -> [Int]
strToInts = map (\x -> (ord x) - 48)

valueIfDup:: Int -> Int -> Int
valueIfDup a b
  | a == b = a
  | a /= b = 0

doPairs:: (Int->Int->Int->Int) -> Int -> [Int] -> Int
doPairs f acc (x:y:ys) = doPairs f (f acc x y) (y:ys)
doPairs _ acc [] = acc
doPairs _ acc [_] = acc

sumDups:: [Int] -> Int
sumDups xs = doPairs
             (\acc x y -> acc + valueIfDup x y)
             (valueIfDup (head xs) (last xs))
             xs
