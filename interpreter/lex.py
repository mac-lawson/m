# Official Language Interpreter for M++
# Official Language Interpreter for M++

import sys
import matplotlib.pyplot as plt
def err(skk): print("\033[91m {}\033[00m" .format(skk))
def fix(skk): print("\033[92m {}\033[00m" .format(skk))

# Graphing Library for M++

def plot_numbers(x, y):
  plt.scatter(x, y)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('M++ Graphing')
  plt.show()

# Math Library for M++
def math(line):
        if(line[0] == "Math.Average"):
            print((float(line[1]) + float(line[3])) / 2)
        if(line[0] == "Math.Max"):
            if(float(line[1]) > float(line[3])):
                print(float(line[1]))
            else:
                print(float(line[3]))
        if(line[0] == "Math.Graph"):
            plot_numbers(float(line[1]), float(line[3]))
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

def lex_file(filename):
    line_num = 1
    with open(filename) as f:
        for line in f:
            words = line.split()
            # Comments and blank spaces
            if("//" in words):
                i = 0
            if(len(words) == 0):
                i = 0
            else:
                globals()[f'line_{line_num}'] = words
                line_num += 1
                # Keep print(words) for debugging
                # print(words)
                try:
                    if("Math" in words[0]):
                        math(words)
                    else:    
                        lex(words)
                except:
                    err("m++ interpreter error")
                    err("line number: " + str(line_num - 1))


try:
    lex_file(sys.argv[1])
except:
    err("m++ error")
    print("No real file was provided to the m++ compiler")
    fix("\nHow to fix: ")
    print("./m++ my_file.m++")