import UIKit
// Sometimes, the scariest thing is to leave the scary thing you already know
// And begin anew, not knowing if you've taken it with you.

// the first 25 numbers are the preamble.
// any other numbers after should be a sum of two of the preamble numbers
// find the first number in other numbers which isn't the sum of two preamble numbers



func getCombos(elements: Array<Int>) -> [[Int]] {
    var list: [[Int]] = []
    for element in elements {
        for complement in elements  {
            list.append([element, complement])
        }
    }
    return list
}


let preambleSize = 25

let fileURL = Bundle.main.url(forResource: "9", withExtension: "txt")
var txt = try String(contentsOf: fileURL!, encoding: String.Encoding.utf8)

txt = txt.trimmingCharacters(in: ["\n"])
let strings = txt.components(separatedBy: "\n")
var lines = [Int]()

for number in strings {
    if let integer = Int(String(number)) {
        lines.append(integer)
    }
}

let numbersForIterating: [Int] = Array(lines.dropFirst(preambleSize))

for (index, number) in numbersForIterating.enumerated() {
    print("Item: ", index)
    let preamble: [Int] = Array(lines[index...preambleSize+index-1])
//    print("Preamble size and first num: ", preamble.count, "-", preamble[0])

    let combos = getCombos(elements: preamble)
//    print("Total combos: ", combos.count)

    var sums: [Int] = []

    for combo in combos {
        if combo.count == 2 {
            sums.append(combo.reduce(0, +))
        }
    }
    
//    print("Total sums to check: ", sums.count)

    if !sums.contains(number) {
        print("We win: ", number)
        break
    }

}




