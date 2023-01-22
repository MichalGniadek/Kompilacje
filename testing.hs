listToSort :: [Int]
listToSort =
  [13, 2, 3, 14, 17, 4, 1, 5, 16, 12, 9, 10, 15, 8, 7, 11, 18, 19, 6, 20]

bubbleSort :: [Int] -> [Int]
bubbleSort lst =
  let bpasses = (bubblePass (lst))
   in if bpasses == lst
        then lst
        else (bubbleSort (bpasses))

bubblePass :: [Int] -> [Int]
bubblePass [] = []
bubblePass [x] = [x]
bubblePass (x1:x2:xs) =
  if x1 > x2
    then [x2] ++ ((bubblePass ([x1] ++ xs)))
    else [x1] ++ ((bubblePass ([x2] ++ xs)))

main = do
  (putStrLn ((show (listToSort))))
  do (putStrLn ((show ((bubbleSort (listToSort))))))
     (return (0))
