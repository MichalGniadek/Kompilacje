    func listToSort() -> [Int] {
        [13, 2, 3, 14, 17, 4, 1, 5, 16, 12, 9, 10, 15, 8, 7, 11, 18, 19, 6, 20]
    }

    func bubbleSort(lst:: [Int]) -> [Int] {
        let bpasses = bubblePass(lst);
        if bpasses == lst {
            lst
        } else{
            bubbleSort(bpasses)
        }
    }

    func bubblePass([]:: [Int]) -> [Int]{
        []
    }

    func bubblePass([x]) {
        [x]
    }

    func bubblePass((x1:x2:xs)){
        if x1 > x2 {
            [x2] ++ (bubblePass([x1] ++ xs))
        } else{
            [x1] ++ (bubblePass([x2] ++ xs))
        }
    }

    func main() {
        do putStrLn(show(listToSort));
        do putStrLn(show(bubbleSort(listToSort)));
        return(0)
    }