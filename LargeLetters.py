#4d 69 6c 6b 65 6e
letters = {
" ": """@     @
@     @
@     @
@     @
@     @
@     @
@     @""",
"a": """@     @
@ xxx @
@x   x@
@xxxxx@
@x   x@
@x   x@
@     @""",
"b": """@     @
@xxxx @
@x   x@
@xxxx @
@x   x@
@xxxx @
@     @""",
"c": """@     @
@ xxx @
@x   x@
@x    @
@x   x@
@ xxx @
@     @""",
"d": """@     @
@xxxx @
@x   x@
@x   x@
@x   x@
@xxxx @
@     @""",
"e": """@     @
@xxxxx@
@x    @
@xxx  @
@x    @
@xxxxx@
@     @""",
"f": """@     @
@xxxxx@
@x    @
@xxxx @
@x    @
@x    @
@     @""",
"g": """@     @
@ xxxx@
@x    @
@x xxx@
@x   x@
@ xxxx@
@     @""",
"h": """@     @
@x   x@
@x   x@
@xxxxx@
@x   x@
@x   x@
@     @""",
"i": """@     @
@ xxx @
@  x  @
@  x  @
@  x  @
@ xxx @
@     @""",
"j": """@     @
@ xxxx@
@    x@
@    x@
@x   x@
@ xxxx@
@     @""",
"k": """@     @
@x   x@
@x  x @
@xxx  @
@x  x @
@x   x@
@     @""",
"l": """@     @
@x    @
@x    @
@x    @
@x    @
@xxxxx@
@     @""",
"m": """@     @
@x   x@
@xx xx@
@x x x@
@x   x@
@x   x@
@     @""",
"n": """@     @
@x   x@
@xx  x@
@x x x@
@x  xx@
@x   x@
@     @""",
"o": """@     @
@ xxx @
@x   x@
@x   x@
@x   x@
@ xxx @
@     @""",
"p": """@     @
@xxxx @
@x   x@
@xxxx @
@x    @
@x    @
@     @""",
"q": """@     @
@ xxx @
@x   x@
@x   x@
@x   x@
@ xxx @
@   x @""",
"r": """@     @
@xxxx @
@x   x@
@xxxx @
@x   x@
@x   x@
@     @""",
"s": """@     @
@ xxxx@
@x    @
@ xxx @
@    x@
@xxxx @
@     @""",
"t": """@     @
@xxxxx@
@  x  @
@  x  @
@  x  @
@  x  @
@     @""",
"u": """@     @
@x   x@
@x   x@
@x   x@
@x   x@
@ xxx @
@     @""",
"v": """@     @
@x   x@
@x   x@
@x   x@
@ x x @
@  x  @
@     @""",
"w": """@     @
@x   x@
@x   x@
@x x x@
@xx xx@
@x   x@
@     @""",
"x": """@     @
@x   x@
@ x x @
@  x  @
@ x x @
@x   x@
@     @""",
"y": """@     @
@x   x@
@ x x @
@  x  @
@  x  @
@  x  @
@     @""",
"z": """@     @
@xxxxx@
@   x @
@  x  @
@ x   @
@xxxxx@
@     @""",
"1": """@     @
@  x  @
@ xx  @
@  x  @
@  x  @
@ xxx @
@     @""",
"2": """@     @
@xxxx @
@    x@
@ xxx @
@x    @
@xxxxx@
@     @""",
"3": """@     @
@xxxx @
@    x@
@xxxx @
@    x@
@xxxx @
@     @""",
"4": """@     @
@x   x@
@x   x@
@ xxxx@
@    x@
@    x@
@     @""",
"5": """@     @
@xxxxx@
@x    @
@xxxx @
@    x@
@xxxx @
@     @""",
"6": """@     @
@ xxx @
@x    @
@xxxx @
@x   x@
@ xxx @
@     @""",
"7": """@     @
@xxxxx@
@    x@
@   x @
@  x  @
@  x  @
@     @""",
"8": """@     @
@ xxx @
@x   x@
@ xxx @
@x   x@
@ xxx @
@     @""",
"9": """@     @
@ xxx @
@x   x@
@ xxx @
@    x@
@ xxx @
@     @""",
"0": """@     @
@ xxx @
@x   x@
@x   x@
@x   x@
@ xxx @
@     @""",
".": """@     @
@     @
@     @
@     @
@     @
@  x  @
@     @""",
"!": """@     @
@  x  @
@  x  @
@  x  @
@     @
@  x  @
@     @""",
"?": """@     @
@ xx  @
@x  x @
@  x  @
@     @
@  x  @
@     @""",
"/": """@     @
@    x@
@   x @
@  x  @
@ x   @
@x    @
@     @""",
"\\": """@     @
@x    @
@ x   @
@  x  @
@   x @
@    x@
@     @""",
"#": """@     @
@ x x @
@xxxxx@
@ x x @
@xxxxx@
@ x x @
@     @""",
"%": """@     @
@x   x@
@   x @
@  x  @
@ x   @
@x   x@
@     @""",
":": """@     @
@     @
@  x  @
@     @
@  x  @
@     @
@     @""",
";": """@     @
@     @
@  x  @
@     @
@  x  @
@ x   @
@     @""",
"(": """@     @
@ x   @
@x    @
@x    @
@x    @
@ x   @
@     @""",
")": """@     @
@   x @
@    x@
@    x@
@    x@
@   x @
@     @""",
}

def letter(letter, separator = " ", width = 10):
    if separator != '@' and len(separator) == 1:
        converted = ""
        for item in letters[letter.lower()].split('\n'):
            line = item.replace('x', f"{letter.upper()*4}").replace(' ', f"{separator*4}").replace('@', separator*width)
            converted += f"{line}\n{line}\n"
        return converted

def word(word, separator = " ", width = 10):
    if separator != '@' and len(separator) == 1:
        converted = ""
        for x in word.lower():
            converted += letter(x, separator, width)
        return converted

def oneline(word, separator = " ", width = 2):
    if separator != '@' and len(separator) == 1:
        line = 0
        converted = ["","","","","","",""]
        for x in word.lower():
            line = 0
            for item in letters[x].split('\n'):
                lines = item.replace('x', f"{x.upper()*4}").replace(' ', f"{separator*4}").replace('@', separator*width)
                converted[line] += lines
                line += 1
        line = 0
        for item in converted:
            converted[line] += '\n'+item
            line += 1
        return '\n'.join(converted)