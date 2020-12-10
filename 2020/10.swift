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

let input = testData.trimmingCharacters(in: .whitespacesAndNewlines).components(separatedBy: .newlines)
var numbers: [Int] = []

print(input)


public let testData: String = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

public let inputData = """
126
38
162
123
137
97
92
67
136
37
146
2
139
74
101
163
128
127
13
111
30
117
3
93
29
152
80
21
7
54
69
40
48
104
110
142
57
116
31
70
28
151
108
20
157
121
47
75
94
39
73
77
129
41
24
44
132
87
114
58
64
4
10
19
138
45
76
147
59
155
156
83
118
109
107
160
61
91
102
115
68
150
34
16
27
135
161
46
122
90
1
164
100
103
84
145
51
60
"""
