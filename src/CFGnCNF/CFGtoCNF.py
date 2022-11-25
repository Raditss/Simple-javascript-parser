def readFile(file):
    with open(file) as cfg:
        conRow = []
        row = cfg.readlines()
        for i in range(len(row)):
            splitRow = row[i].replace("->", "").split()
            conRow.append(splitRow)
    return conRow

def addRule(rule):
    global dict
    if rule[0] not in dict:
        dict[rule[0]] = []
    dict[rule[0]].append(rule[1:])

def convertCFG(grammar):
    global dict
    product, result = [], []
    i = 0
    for rule in grammar:
        newrule = []
        if len(rule) == 2 and not rule[1][0].islower():
            product.append(rule)
            addRule(rule)
            continue
        while len(rule) > 3:
            newrule.append([f"{rule[0]}{i}", rule[1], rule[2]])
            rule = [rule[0]] + [f"{rule[0]}{i}"] + rule[3:]
            i += 1
        if rule:
            addRule(rule)
            result.append(rule)
        if newrule:
            for i in range(len(newrule)):
                result.append(newrule[i])
    while product:
        rule = product.pop() 
        if rule[1] in dict:
            for item in dict[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0].islower():
                    result.append(new_rule)
                else:
                    product.append(new_rule)
                addRule(new_rule)
    return result

def grammarMapping(grammar):
    map = {}
    for rule in grammar :
        map[str(rule[0])] = []
    for rule in grammar :
        elmt = []
        for iRule in range(1, len(rule)) :
            apd = rule[iRule]
            elmt.append(apd)
        map[str(rule[0])].append(elmt)
    return map

dict = {}