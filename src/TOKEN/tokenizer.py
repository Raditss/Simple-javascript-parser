import os
import sys 
import re

def matching(text, exprs):
    pos = 0             # absolute position
    currPos = 1         # position in relative to line
    line = 1            # current line
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1
            currPos = 1

        flag = None
        for tokenExpr in tokenExprs:
            pattern, tag = tokenExpr    
            regex = re.compile(pattern)
            flag = regex.match(text, pos)
            if flag:
                if tag:
                    token = tag
                    tokens.append(token)
                break
        if not flag:
            print(f"\nSYNTAX ERROR\n Variabel tidak boleh dimulai dengan simbol {text[pos]}")
            sys.exit(1)
        else:
            pos = flag.end(0)
        currPos += 1

    return tokens

tokenExprs = [
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
    (r'\->',            "ARROW"),
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
    (r'\bis\b',                 "IS"),
    (r'\bfunction\b',           "FUNC"),
    (r'\breturn\b',             "RETURN"),
    (r'\braise\b',              "RAISE"),
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
    # variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VAR"),
    ]

def createToken(text):
    tkn = open(text, encoding="utf8")
    characters = tkn.read()
    tkn.close()

    tokens = matching(characters, tokenExprs)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)


    # Write file
    path = os.getcwd()
    tkn = open("TOKEN/tokenResult.txt", 'w')
    for token in tokenResult:
        tkn.write(str(token)+" ")
        # print(token)
    tkn.close()

    return tokenResult