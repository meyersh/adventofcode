import Data.List (sort)

-- Part 1. Find the "checksum"
reds :: Eq a => Int -> Int -> [a] -> (Int,Int)
-- Iterate thru, three at a time.
reds p t (a:b:c:ds)
  | a /= b && b == c = reds p t (b:c:ds)
  | a == b && b /= c = reds 1 t (c:ds)
  | a == b && b == c = reds p 1 ds
  | a /= b && b /= c = reds p t (c:ds)
-- Check the last two. (Needed to correct the numbers on my input.)
reds p t (a:b:cs)
  | a == b = reds 1 t cs
  | a /= b = reds p t cs
reds p t _ = (p, t)

-- Part 2. Find the pair differing by only one place.
rmdupl :: Eq a => [a] -> [a] -> [a]
rmdupl s s' = fst $ unzip $ filter (\(a,b) -> if a == b then True else False) $ zip s s'


-- To make the pairwise pieces, I'm picturing something like
-- *Main> take 9 $ zip (cycle [1,2,3]) (cycle [2,3])
-- [(1,2),(2,3),(3,2),(1,3),(2,2),(3,3),(1,2),(2,3),(3,2)]

main = do
  contents <- readFile "inputs/day2.txt"
  let codes = lines contents
  let reduns = map (\s -> reds 0 0 $ sort s) codes
  let (dubs,trips) =  foldl (\(x,y) (x',y') -> (x+x',y+y')) (0,0) reduns
  print dubs
  print trips
  print $ dubs * trips
  
