import Data.Char (isDigit)
import Data.List (findIndex)

data Shape = Circle Point Float | Rectangle Point Point deriving (Show)  

data Person = Person { firstName :: String  
                     , lastName :: String  
                     , age :: Int  
                     , height :: Float  
                     , phoneNumber :: String  
                     , flavor :: String  
                     } deriving (Show)   

data Maybe' a = Nothing' | Just' a  

data Car a b c = Car { company :: a  
                     , model :: b  
                     , year :: c   
                     } deriving (Show)  


data (Ord k) => Map k v = ...  

class Eq a where  
    (==) :: a -> a -> Bool  
    (/=) :: a -> a -> Bool  
    x == y = not (x /= y)  
    x /= y = not (x == y)  

instance Eq TrafficLight where  
    Red == Red = True  
    Green == Green = True  
    Yellow == Yellow = True  
    _ == _ = False  

a = 23

main = do
  file <- readFile "input.txt"
  let ls = lines file
      nums = map (fst . parseSnailfish 0) ls
      increaseLevel = map (\(x, l) -> (x, l + 1))
      calc a b = reduceSnailfish (increaseLevel a ++ increaseLevel b)
      result = foldl1 calc nums
  print (mag result)

parseSnailfish :: Num t => t -> [Char] -> ([(Int, t)], [Char])
parseSnailfish level str =
  if head str == '['
    then
      let (a, str') = parseSnailfish (level + 1) (tail str)
          (b, str'') = parseSnailfish (level + 1) (tail str')
       in (a ++ b, tail str'')
    else
      let (num, str') = span isDigit str
       in ([(read num :: Int, level)], str')

mag nums =
  case findIndex (\i -> snd (nums !! i) == snd (nums !! (i + 1))) [0 .. (length nums - 2)] of
    Just i -> mag $ concatMap (index i) [0 .. (length nums -1)]
    Nothing -> fst $ head nums
  where
    index i j
      | j == i = [(3 * fst (nums !! i) + 2 * fst (nums !! (i + 1)), snd (nums !! i) - 1)]
      | j == (i + 1) = []
      | otherwise = [nums !! j]
f 1 = 123
f _ = 123

f a = case a of
      1 -> asd
      2 -> asd

reduceSnailfish num =
  let num' = explode num
   in if num /= num'
        then reduceSnailfish num'
        else
          let num'' = split num
           in if num /= num''
                then reduceSnailfish num''
                else num''

explode :: [(Int, Int)] -> [(Int, Int)]
explode nums =
  let explosion i j
        | j == (i -1) = (fst (nums !! j) + fst (nums !! i), snd (nums !! j))
        | j == i = (0, snd (nums !! i) - 1)
        | j == (i + 2) = (fst (nums !! j) + fst (nums !! (i + 1)), snd (nums !! j))
        | otherwise = nums !! j
   in case findIndex (\x -> snd x > 4) nums of
        Just i -> [explosion i j | j <- [0 .. (length nums -1)], j /= (i + 1)]
        Nothing -> nums

split :: [(Int, Int)] -> [(Int, Int)]
split nums = case findIndex (\x -> fst x >= 10) nums of
  Just i -> concatMap (splt i) (zip nums [0 ..])
  Nothing -> nums
  where
    splt i ((x, l), j)
      | i /= j = [(x, l)]
      | even x = [(x `div` 2, l + 1), (x `div` 2, l + 1)]
      | otherwise = [(x `div` 2, l + 1), (x `div` 2 + 1, l + 1)]