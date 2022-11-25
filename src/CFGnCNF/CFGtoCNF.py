import keyword

terminal = keyword.kwlist

dict = {}

def readFile(file):
  with open(file) as cfg_file:
    baris = cfg_file.readlines()
    convert = []
    for i in range(len(baris)):
      splits = baris[i].replace("->", "").split()
      convert.append(splits)
  return convert

def addRule(rule):
  global dict
  if rule[0] not in dict:
    dict[rule[0]] = []
  dict[rule[0]].append(rule[1:])

def convertGrammar(grammar):
    global dict
    x = 0
    prod, res = [], []
    for rule in grammar:
      new = []
      if len(rule) == 2 and not rule[1][0].islower() :
        prod.append(rule)
        addRule(rule)
        continue
      while len(rule) > 3:
        
        new.append([f"{rule[0]}{x}", rule[1], rule[2]])
        rule = [rule[0]] + [f"{rule[0]}{x}"] + rule[3:]
        x += 1
      if rule:
        addRule(rule)
        res.append(rule)
      if new:
        for i in range(len(new)):
          res.append(new[i])
    while prod:
      rule = prod.pop() 
      if rule[1] in dict:
        for item in dict[rule[1]]:
          new = [rule[0]] + item
          if len(new) > 2 or new[1][0].islower():
            res.append(new)
          else:
            prod.append(new)
          addRule(new)
    return res

def grammarMapping(grammar):
  map = {}
  for rule in grammar :
    map[str(rule[0])] = []
  for rule in grammar :
    elmt = []
    for ruleI in range(1, len(rule)) :
      apd = rule[ruleI]
      elmt.append(apd)
    map[str(rule[0])].append(elmt)
  return map

def writeGrammar(grammar):
    file = open('cnf.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

if __name__ == "__main__":
  writeGrammar(convertGrammar((readFile("cfg.txt")))) 