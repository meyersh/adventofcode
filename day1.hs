-- `cycle` creates and endless cycle from a list (perfect for repeat
-- processing.)
--

-- Initial set: (S.fromList [])
-- Add x: (S.insert x $ s.fromList [])
-- Check for x: (S.member x $ s.fromList [])

-- part 2 setup.
import qualified Data.IntSet as S
import Data.IntSet (IntSet)

-- mfw leading '+' breaks read. wthcc??
read' ('+':xs) = read xs
read' x        = read x

pt2 currentFrequency seen (c:changes) =
  if S.member nextFrequency seen then
    nextFrequency
  else
    pt2 nextFrequency (S.insert nextFrequency seen) changes
  where
    nextFrequency = currentFrequency + c
  

main = do
  contents <- readFile "inputs/day1a.txt"
  let changes = map read' $ lines contents :: [Int]

  -- Part A.
  print $ sum changes

  -- Part B.
  print $ pt2 0 (S.fromList []) (cycle changes)

  
