letters = {
"a": """-     -
- xxx -
-x   x-
-xxxxx-
-x   x-
-x   x-
-     -""",
"b": """-     -
-xxxx -
-x   x-
-xxxx -
-x   x-
-xxxx -
-     -""",
"c": """-     -
- xxx -
-x   x-
-x    -
-x   x-
- xxx -
-     -""",
"d": """-     -
-xxxx -
-x   x-
-x   x-
-x   x-
-xxxx -
-     -""",
"e": """-     -
-xxxxx-
-x    -
-xxx  -
-x    -
-xxxxx-
-     -""",
"f": """-     -
-xxxxx-
-x    -
-xxxx -
-x    -
-x    -
-     -""",
"g": """-     -
- xxxx-
-x    -
-x xxx-
-x   x-
- xxxx-
-     -""",
"h": """-     -
-x   x-
-x   x-
-xxxxx-
-x   x-
-x   x-
-     -""",
"i": """-     -
- xxx -
-  x  -
-  x  -
-  x  -
- xxx -
-     -""",
"j": """-     -
- xxxx-
-    x-
-    x-
-x   x-
- xxxx-
-     -""",
"k": """-     -
-x   x-
-x  x -
-xxx  -
-x  x -
-x   x-
-     -""",
"l": """-     -
-x    -
-x    -
-x    -
-x    -
-xxxxx-
-     -""",
"m": """-     -
-x   x-
-xx xx-
-x x x-
-x   x-
-x   x-
-     -""",
"n": """-     -
-x   x-
-xx  x-
-x x x-
-x  xx-
-x   x-
-     -""",
"o": """-     -
- xxx -
-x   x-
-x   x-
-x   x-
- xxx -
-     -""",
"p": """-     -
-xxxx -
-x   x-
-xxxx -
-x    -
-x    -
-     -""",
"q": """-     -
- xxx -
-x   x-
-x   x-
-x   x-
- xxx -
-   x -""",
"r": """-     -
-xxxx -
-x   x-
-xxxx -
-x   x-
-x   x-
-     -""",
"s": """-     -
- xxxx-
-x    -
- xxx -
-    x-
-xxxx -
-     -""",
"t": """-     -
-xxxxx-
-  x  -
-  x  -
-  x  -
-  x  -
-     -""",
"u": """-     -
-x   x-
-x   x-
-x   x-
-x   x-
- xxx -
-     -""",
"v": """-     -
-x   x-
-x   x-
-x   x-
- x x -
-  x  -
-     -""",
"w": """-     -
-x   x-
-x   x-
-x x x-
-xx xx-
-x   x-
-     -""",
"x": """-     -
-x   x-
- x x -
-  x  -
- x x -
-x   x-
-     -""",
"y": """-     -
-x   x-
- x x -
-  x  -
-  x  -
-  x  -
-     -""",
"z": """-     -
-xxxxx-
-   x -
-  x  -
- x   -
-xxxxx-
-     -""",
}

def letter(letter, separator = " ", width = 10):
    converted = ""
    for item in letters[letter].split('\n'):
        line = item.replace('x', f"{letter.upper()*4}").replace(' ', f"{separator*4}").replace('-', separator*width)
        converted += f"{line}\n{line}\n"
    return converted

def word(word, separator = " ", width = 10):
    converted = ""
    for x in word:
        converted += letter(x, separator)
    return converted