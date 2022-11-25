from CFGnCNF.CFGtoCNF import readFile, convertCFG, grammarMapping
from TOKEN.tokenizer import createToken
from CYK.CYK import CYKParser
import argparse

def splashScreen() :
  print("███╗   ██╗     ██████╗     ██████╗     ███████╗                ██╗    ███████╗             ")
  print("████╗  ██║    ██╔═══██╗    ██╔══██╗    ██╔════╝                ██║    ██╔════╝             ")      
  print("██╔██╗ ██║    ██║   ██║    ██║  ██║    █████╗                  ██║    ███████╗             ")
  print("██║╚██╗██║    ██║   ██║    ██║  ██║    ██╔══╝             ██   ██║    ╚════██║             ")
  print("██║ ╚████║    ╚██████╔╝    ██████╔╝    ███████╗    ██╗    ╚█████╔╝    ███████║             ") 
  print("╚═╝  ╚═══╝     ╚═════╝     ╚═════╝     ╚══════╝    ╚═╝     ╚════╝     ╚══════╝             ")
  print(" ██████╗     ██████╗     ███╗   ███╗    ██████╗     ██╗    ██╗         ███████╗    ██████╗ ")
  print("██╔════╝    ██╔═══██╗    ████╗ ████║    ██╔══██╗    ██║    ██║         ██╔════╝    ██╔══██╗")
  print("██║         ██║   ██║    ██╔████╔██║    ██████╔╝    ██║    ██║         █████╗      ██████╔╝")
  print("██║         ██║   ██║    ██║╚██╔╝██║    ██╔═══╝     ██║    ██║         ██╔══╝      ██╔══██╗")
  print("╚██████╗    ╚██████╔╝    ██║ ╚═╝ ██║    ██║         ██║    ███████╗    ███████╗    ██║  ██║")
  print(" ╚═════╝     ╚═════╝     ╚═╝     ╚═╝    ╚═╝         ╚═╝    ╚══════╝    ╚══════╝    ╚═╝  ╚═╝")   

def result():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = argparse.FileType('r'))
    args = parser.parse_args()
    splashScreen()
    print("\nLoading...")
    print("Checking your codes...")
    print("File name: " + str(args.file.name.split('/')[len(args.file.name.split('/'))-1]) + "\n")
    token = createToken(args.file.name)
    token = [x.lower() for x in token]
    CNF = grammarMapping(convertCFG((readFile("CFGnCNF/CFG.txt"))))
    print("=======================RESULT=========================\n")
    CYKParser(token, CNF)
    print("======================================================")

if __name__ == "__main__":
    result()