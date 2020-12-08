import UIKit
import PlaygroundSupport


var str = "Hello, playground"

// 8.txt has one instruction per line of text.
// Follow them until you run an instruction a second time
// then print the accumulator's value.

let fileURL = Bundle.main.url(forResource: "8_test", withExtension: "txt")
var txt = try String(contentsOf: fileURL!, encoding: String.Encoding.utf8)
print(txt)


