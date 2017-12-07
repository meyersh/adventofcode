day3input = 265149 :: Double


-- Figure out the "manhattan" or "Tax-cab" distance for a given square to 1.
-- 17  16  15  14  13
-- 18   5   4   3  12
-- 19   6   1   2  11
-- 20   7   8   9  10
-- 21  22  23---> ...

-- 1x1
-- 3x3 (1+2x1+2)
-- 5x5 (3+2x3+2)

-- Square area raising by n^2 for n = 2k+1 | k = 0, 1, 2, 3, ...
squares = [((2*n+1)^2, (2*n+3)^2) | n <- [0..]]

whatSquareAreWeIn 1 = (1,1)
whatSquareAreWeIn n = last $ takeWhile( \(from, to) -> n >= to || from < n && n <= to) squares

normalizeSquare (x,y) = (x-x, y-x)

normalizeN n = (\(x,y) -> n-x) $ whatSquareAreWeIn n

-- to minus from minus four corners / 4 gives us face length.
sideLength (from,to) = ((to-from-4) / 4) + 2

perimeter (from,to) = to - from

-- Add to a component of an ordered pair.
yplus (x,y) n = (x,   y+n)
xplus (x,y) n = (x+n, y)

-- for half a face we're moving +, for half we're -, and for the midpoint we're 0.

normalizeSquareToCoords n
  | edgeDistance < faceLength     =
      yplus endingCoords (edgeDistance)
  | edgeDistance < ((faceLength)* 2 )- 1 =
      xplus (yplus endingCoords (faceLength-1)) (-1*(edgeDistance - (faceLength))-1)
  | edgeDistance <= ((faceLength-1) * 3) =
      yplus (xplus endingCoords (-faceLength + 1)) (-(edgeDistance-(faceLength-1)*2)+faceLength-1)
  | otherwise =
      xplus endingCoords (edgeDistance - ((faceLength-1)* 4))

  where
    -- n =  0, 1, 2, 3, ...
    ourSquare  = whatSquareAreWeIn n
    edgeRange  = normalizeSquare ourSquare
    faceLength = sideLength ourSquare
    edgeDistance = normalizeN n

    -- The "ending" coordinates for this sequence, the bottom-right side.
    endingCoords = ((faceLength - 1)/2, (faceLength - 1)/(-2))

manhattanDistance (x,y) = (abs x) + (abs y)

main =
  do
    putStrLn $ show $ manhattanDistance . normalizeSquareToCoords $ day3input
