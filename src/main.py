from CFGnCNF.CFGtoCNF import readFile, convertCFG, grammarMapping
from TOKEN.tokenizer import createToken
from CYK.CYK import cykParse
import re, os, sys, argparse

def bannerCompiler() :
  print("███╗   ██╗     ██████╗     ██████╗     ███████╗                ██╗    ███████╗ ")
  print("████╗  ██║    ██╔═══██╗    ██╔══██╗    ██╔════╝                ██║    ██╔════╝ ")      
  print("██╔██╗ ██║    ██║   ██║    ██║  ██║    █████╗                  ██║    ███████╗ ")
  print("██║╚██╗██║    ██║   ██║    ██║  ██║    ██╔══╝             ██   ██║    ╚════██║ ")
  print("██║ ╚████║    ╚██████╔╝    ██████╔╝    ███████╗    ██╗    ╚█████╔╝    ███████║ ") 
  print("╚═╝  ╚═══╝     ╚═════╝     ╚═════╝     ╚══════╝    ╚═╝     ╚════╝     ╚══════╝             ")
  print(" ██████╗     ██████╗     ███╗   ███╗    ██████╗     ██╗    ██╗         ███████╗    ██████╗ ")
  print("██╔════╝    ██╔═══██╗    ████╗ ████║    ██╔══██╗    ██║    ██║         ██╔════╝    ██╔══██╗")
  print("██║         ██║   ██║    ██╔████╔██║    ██████╔╝    ██║    ██║         █████╗      ██████╔╝")
  print("██║         ██║   ██║    ██║╚██╔╝██║    ██╔═══╝     ██║    ██║         ██╔══╝      ██╔══██╗")
  print("╚██████╗    ╚██████╔╝    ██║ ╚═╝ ██║    ██║         ██║    ███████╗    ███████╗    ██║  ██║")
  print(" ╚═════╝     ╚═════╝     ╚═╝     ╚═╝    ╚═╝         ╚═╝    ╚══════╝    ╚══════╝    ╚═╝  ╚═╝")   
  print()

def verdict():
  # Argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()

  # Banner and verdict
  bannerCompiler()
  print("\nLoading...")
  print("Checking your codes...")
  print("File name: " + str(args.file.name.split('/')[len(args.file.name.split('/'))-1]))
  print()
  
  # Token & CNF
  token = createToken(args.file.name)
  token = [x.lower() for x in token]
  CNFgrammar = grammarMapping(convertCFG((readFile("CFGnCNF/CFG.txt"))))
  print("======================VERDICT=========================")
  print()
  cykParse(token, CNFgrammar)
  print()
  print("======================================================")

if __name__ == "__main__":
  verdict()