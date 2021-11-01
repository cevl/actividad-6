import json
import re

file = open("read.py")

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'ent' : 'integer type', 'flot': 'Floating point' , 'car' : 'Character type', 'grande' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { 'print': 'function' }
identifier_key = identifier.keys()

reserved = ['mientras', 'para', 'romper', 'continuar', 'retornar', 'si', 'funcion']

translate = {'mientras' : 'while', 'para' : 'for', 'romper' : 'break', 'continuar' : 'continue',
             'retornar' : 'return', 'si' : 'if', 'funcion' : 'function', 'ent' : 'let', 'flot' : 'let',
             'car' : 'let', 'grande' : 'let', '=' : '=', '+' : '+', '-' : '-', '/' : '/', '*' : '*', '<' : '<', '>' : '>'}

a=file.read()

count=0
program = a.split("\n")
jprogram = []
for line in program:
    count = count + 1
    #print("line#" , count, "\n" , line)
                
    tokens=line.split(' ')
    
    if tokens[0] in data_type_key:
            if tokens[1] not in identifier:
                identifier[tokens[1]] = 'id'
                identifier_key = identifier.keys()
                
    jtokens = []
    for token in tokens:
        if token in operators_key:
            jtokens.append(token)
        elif token in data_type_key:
            jtokens.append(token)
        elif token in punctuation_symbol_key:
            jtokens.append(token)
        elif token in identifier_key:
            jtokens.append(token)
        elif re.match('[0-9]*', token):
            jtokens.append(token)
        elif re.match('"[0-9 a-z A-Z]*"'):
            jtokens.append(translate(token))
    
    jprogram.append(jtokens);
json_object = json.dumps(jprogram, indent = 4)
with open("jprogram.json", "w") as outfile:
    outfile.write(json_object)
    
def translate(token):
    jtoken = translate[token]
    return token
