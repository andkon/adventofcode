//: [Previous](@previous)

import Foundation
import UIKit

// whoops that all disappeared
// find a contiguous set of numbers which add up to the SOLUTION
// add together the smallest and largest number in this range
let SOLUTION = 22477624
// 22477624


let fileURL = Bundle.main.url(forResource: "9", withExtension: "txt")
var txt = try String(contentsOf: fileURL!, encoding: String.Encoding.utf8)
let trimmedText = txt.trimmingCharacters(in: .whitespacesAndNewlines)
let lines = trimmedText.components(separatedBy: "\n")

var numbers: [Int] = []

for number in lines {
    if let num = Int(number) {
        numbers.append(num)
    }
}

var solved = false

for (index, number) in numbers.enumerated() {
    // loop through, adding all subsequent numbers to see if you get one
    let remainder = numbers.dropFirst(index)
    
    
    
    for (i, add) in remainder.enumerated() {
        // make array slice
        let slice = remainder.prefix(i)
        // reduce array slice
        if slice.reduce(0, +) == SOLUTION {
            let sorted = slice.sorted()
            print("We win! Starts with ", sorted.first!, " and ends with ", sorted.last!, "which make ", (sorted.first! + sorted.last!))
            solved = true
            break
        }
        
        
    }
    if solved == true {
        break
    }
}


//: [Next](@next)
