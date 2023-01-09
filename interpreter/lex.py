# Official Language Interpreter for M++
# Official Language Interpreter for M++


import sys

# Math Library for M++
def math(line):
    if(line[0] == "Math.Average"):
        print((float(line[1]) + float(line[3])) / 2)

# Official Lexer for M++
# All language libraries should be applied
def lex(line):  
    if(line[0] == "add"):
        print(float(line[1]) + float(line[3]))
    if(line[0] == "subtract"):
        print(float(line[1]) - float(line[3]))
    if(line[0] == "divide"):
        print(float(line[1]) / float(line[3]))
    if(line[0] == "return"):
        print(str(line[1]))
    if(line[0] == "breakln()"):
        print("")

def process_file(filename):
    line_num = 1
    with open(filename) as f:
        for line in f:
            words = line.split()
            globals()[f'line_{line_num}'] = words
            line_num += 1
            # Keep print(words) for debugging
            # print(words)
            if("Math" in words):
                math(words)
            else:    
                lex(words)

# Example usage
process_file('demo.m++')

