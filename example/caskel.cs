from Data.Char include isDigit;
from Data.List include findIndex;

struct Shape Circle(Int, Int) | Rectangle(Float, Float);
struct Shape Circle{
    a: Int,
    b: Int,
} | Rectangle{
    a: Float,
    b: Float
} implementing Show;

struct Maybe<T: Ord> Nothing | Just(T);

interface Eq(T) {
    func (==)(a: T, b: Y) -> Bool;
}

implement Eq for Trafficlight {
    func (==)(a, b){
        cośtam
    }
}

func main() {
    do file <- readFile("input.txt");
    let ls = lines file;
    let nums = map(func(x, l) {(x, l+1)});
    do print(mag(result));
}

func parseSnailfish(level, str) {
    if head(str) == '[' {
        let (a, str') = parseSnailfish(level + 1, tail(str));
        let (b, str'') = parseSnailfish(level + 1, tail(str'));
        (a ++ b, tail (str''))
    } else {
        let (num, str') = span(isDigit(str));
        ([read(num), level], str')
    }
}

func split(nums) {
    switch(find(index)) {
        case Just(i) {
            
        }
        case Nothing {

        }
    }
}