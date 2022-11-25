import os
import sys 
import re

def matching(text, exprs):
    pos = 0 
    line = 1
    tokens = []
    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
        flag = None
        for tokenExpr in exprs:
            pattern, temp = tokenExpr    
            regex = re.compile(pattern)
            flag = regex.match(text, pos)
            if flag:
                if temp:
                    token = temp
                    tokens.append(token)
                break
        if not flag:
            print(f"\nSYNTAX ERROR\n Terdapat error pada line {line}")
            sys.exit(1)
        else:
            pos = flag.end(0)

    return tokens

exprs = [
    # Not token
    (r'[ \t]+',                                      None),
    (r'//[^\n]*',                                    None),
    (r'/\*[^\/\*]*\*/',                              "MULTILINE"),
    (r'\;',                                          "SCOLON"),
    (r'\n',                                          "NEWLINE"),

    # Operator
    (r'\=(?!\=)',       "EQUAL"),
    (r'\===',           "ISEQQ"),
    (r'\!==',           "NEQQ"),
    (r'\==',            "ISEQ"),
    (r'!=',             "NEQ"),
    (r'<=',             "LE"),
    (r'<',              "L"),
    (r'>=',             "GE"),
    (r'>',              "G"),
    (r'\(',             "LB"),
    (r'\)',             "RB"),
    (r'\[',             "LSB"),
    (r'\]',             "RSB"),
    (r'\{',             "LCB"),
    (r'\}',             "RCB"),
    (r'\:',             "COLON"),
    (r'\;',             "SCOLON"),
    (r'-=',             "SUBTREQ"),
    (r'\*=',            "MULEQ"),
    (r'\+=',            "SUMEQ"),
    (r'/=',             "DIVEQ"),
    (r'\+',             "ADD"),
    (r'\-',             "SUBTR"),
    (r'\*\*',           "POW"),
    (r'\*',             "MUL"),
    (r'/',              "DIV"),
    (r'\,',             "COMMA"),
    (r'\.',             "DOT"),
    (r'\%',             "MOD"),
    (r'\&\&',             "AND"),
    (r'\|\|',             "OR"),



    # Type
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'\bdict\b',               "TYPE"),
    (r'\bint\b',                "TYPE"),
    (r'\bstr\b',                "TYPE"),
    (r'\bfloat\b',              "TYPE"),
    (r'\bcomplex\b',            "TYPE"),
    (r'\blist\b',               "TYPE"),
    (r'\btuple\b',              "TYPE"),

    # keyword
    (r'\btrue\b',               "TRUE"),
    (r'\bfalse\b',              "FALSE"),
    (r'\bNone\b',               "NONE"),
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\belif\b',               "ELIF"),
    (r'\bfor\b',                "FOR"),
    (r'\bin\b',                 "IN"),
    (r'\brange\b',              "RANGE"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bpass\b',               "PASS"),
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bas\b',                 "AS"),
    (r'\bfunction\b',           "FUNC"),
    (r'\breturn\b',             "RETURN"),
    (r'\bwith\b',               "WITH"),
    (r'\bclass\b',              "CLASS"),
    (r'\bvar\b',                "AVAR"),
    (r'\bconst\b',              "ACONST"),
    (r'\blet\b',                "ALET"),
    (r'\btry\b',                "TRY"),
    (r'\bcatch\b',               "CATCH"),
    (r'\bfinally\b',            "FINALLY"),
    (r'\bswitch\b',             "SWITCH"),
    (r'\bcase\b',               "CASE"),
    (r'\bdefault\b',            "DEFAULT"),
    (r'\bdelete\b',            "DELETE"),
    (r'\bdo\b',            "DO"),
    # variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VAR"),
    ]

def createToken(text):
    tkn = open(text, encoding="utf8")
    chara = tkn.read()
    tkn.close()

    tokens = matching(chara, exprs)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)
    path = os.getcwd()
    tkn = open("TOKEN/tokenResult.txt", 'w')
    for token in tokenResult:
        tkn.write(str(token)+" ")
    tkn.close()

    return tokenResult