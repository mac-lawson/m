# Official Language Interpreter for M++
# Official Language Interpreter for M++
class errors:
    file = "No real file was provided to the m++ compiler"
import sys
import matplotlib.pyplot as plt
import subprocess
def err(skk): print("\033[91m {}\033[00m" .format(skk))
def fix(skk): print("\033[92m {}\033[00m" .format(skk))

# Multiword String management
def put(line):
    for i in range(1,len(line)):
        if i != len(line): 
            print(line[i], end=' ')
        else:
            print(line[i], end='')
    print("\n")


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
    # BASIC MATH
    if(line[0] == "add"):
        print(float(line[1]) + float(line[3]))
    if(line[0] == "subtract"):
        print(float(line[1]) - float(line[3]))
    if(line[0] == "divide"):
        print(float(line[1]) / float(line[3]))
    if(line[0] == "multiply"):
        print(float(line[1]) * float(line[3]))
    if(line[0] == "mod"):
        print(float(line[1]) % float(line[3]))
    
    # STRING HANDLING
    if(line[0] == "put"):
        put(line)
    if(line[0] == "breakln()"):
        print("")




# Function that interprets files
def lex_file(filename):
    import re
    line_num = 1
    with open(filename) as f:
        for line in f:
            words = re.findall(r'\b\w+\b', line)
            if("//" in words):
                continue
            if(len(words) == 0):
                continue
            else:
                quoted_strings = [word for word in words if '"' in word]
                if quoted_strings:
                    quoted_string = ' '.join(word.replace('"','') for word in quoted_strings)
                    words = [word for word in words if '"' not in word]
                    words.append(quoted_string)
                    globals()[f'line_{line_num}'] = words
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
    print(errors.file)
    fix("\nHow to fix: ")
    print("./m++ my_file.m++")