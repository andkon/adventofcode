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

// the device: highest adapter + 3
// adapters: start with lowest, pick next based on lowest that still is only 1, 2 or 3 higher
// the outlet: 0. Start there!



let fileURL = Bundle.main.url(forResource: "10_test", withExtension: "txt")
let txt = try String(contentsOf: fileURL!, encoding: String.Encoding.utf8)

let input = txt.trimmingCharacters(in: .whitespacesAndNewlines).components(separatedBy: .newlines)

var numbers: [Int] = []

print(input)
