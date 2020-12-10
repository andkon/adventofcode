//
//  10.swift
//
//
//  Created by Andrew Konoff on 2020-12-10.
//
import Foundation

// Make a change, and a thousand should follow.
// That's what the vulnerable feeling is about:
// How much might I get lost in all those changes?
// And that's scarier when you're barely there to begin with.

// you have a bunch of joltage adapters, with a specific output joltage.
// they can TAKE 1, 2 or 3 jolts lower than its output rating & still output the rated joltage
// also, your device can take 3 jolts higher than the highest adapter in your bag.
// the charging outlet's joltage rating is 0.

// Use every adapter at once, and find out the gap in each step between the outlet, adapters, and device.
// multiply the number of one jolt differences by the number of 3 jolt differences

// the device: highest adapter + 3
// adapters: start with lowest, pick next based on lowest that still is only 1, 2 or 3 higher
// the outlet: 0. Start there!

let fileURL = Bundle.main.url(forResource: "10", withExtension: "txt")
let txt = try String(contentsOf: fileURL!, encoding: String.Encoding.utf8)

let input = txt.trimmingCharacters(in: .whitespacesAndNewlines).components(separatedBy: .newlines)

var adapters: [Int] = []

for number in input {
    if let num = Int(number) {
        adapters.append(num)
    }
}
adapters.sort()
print(adapters)
var differences: [Int:Int] = Dictionary()

var lastJolt = 0

for adapter in adapters {
//    print("Adapter: ", adapter)
    let difference = adapter - lastJolt
    print("Difference: ", difference)
    differences[difference] = (differences[difference] ?? 0) + 1
    lastJolt = adapter
}

differences[3] = differences[3]! + 1 // for the in-device adapter

print("There are ", differences[1], " 1 jolt differences and ", differences[3], "3 jolt differences")
let soln = differences[1]! * differences[3]!
print("Answer is: ", soln)
