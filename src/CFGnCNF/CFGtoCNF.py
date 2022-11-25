import keyword

terminal = keyword.kwlist

dict = {}

#Read txt
def readFile(file):
    with open(file) as cfg_file:
        baris = cfg_file.readlines()
        barisConverted = []
        for i in range(len(baris)):
            splitBaris = baris[i].replace("->", "").split()
            barisConverted.append(splitBaris)
    return barisConverted


#Adding rule to global var
def addRule(rule):
  global dict
  
  if rule[0] not in dict:
    dict[rule[0]] = []
  dict[rule[0]].append(rule[1:])

def convertGrammar(grammar):
    global dict
    idx = 0
    unitProductions, res = [], []
    for rule in grammar:
      new_rules = []
      # buat yang cuma satu nonterminal/terminal di kanan
      if len(rule) == 2 and not rule[1][0].islower() :
        unitProductions.append(rule)
        addRule(rule)
        continue
      # Proses if lebih dari 3 nonterminalnya ini bakal di split jadi cuma 3 doang  
      while len(rule) > 3:
        
        new_rules.append([f"{rule[0]}{idx}", rule[1], rule[2]])
        rule = [rule[0]] + [f"{rule[0]}{idx}"] + rule[3:]
        idx += 1
      if rule:
        addRule(rule)
        res.append(rule)
      if new_rules:
        for i in range(len(new_rules)):
          res.append(new_rules[i])

    # Proses cuma yang ada 1 non terminal di kanan
    while unitProductions:
      rule = unitProductions.pop() 
      if rule[1] in dict:
        for item in dict[rule[1]]:
          new_rule = [rule[0]] + item
          # nonterminal dikanan bakal dirubah either kalo panjangnya 3 / ada terminal
          if len(new_rule) > 2 or new_rule[1][0].islower():
            res.append(new_rule)
          #Kalo cuma 2 tp dia bukan terminal masukin lg ke production ujungnya bakal dirubah jadi terminal
          else:
            unitProductions.append(new_rule)
          addRule(new_rule)
    return res

def grammarMapping(grammar):
  map = {}
  for rule in grammar :
    map[str(rule[0])] = []
  for rule in grammar :
    elmt = []
    for idxRule in range(1, len(rule)) :
      apd = rule[idxRule]
      elmt.append(apd)
    map[str(rule[0])].append(elmt)
  return map

def writeGrammar(grammar):
    cnf = open('CNF.txt', 'w')
    for rule in grammar:
        cnf.write(rule[0])
        cnf.write(" -> ")
        for i in rule[1:]:
            cnf.write(i)
            cnf.write(" ")
        cnf.write("\n")
    cnf.close()

if __name__ == "__main__":
  writeGrammar(convertGrammar((readFile("CFG.txt")))) 