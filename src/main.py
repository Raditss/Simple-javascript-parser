from CFGtoCNF import readGrammarFile, convertGrammar, mapGrammar
from tokenizer import createToken
from parser1 import cykParse
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
  print("File name: " + str(args.file.name))
  print()
  
  # Token & CNF
  token = createToken(args.file.name)
  token = [x.lower() for x in token]
  CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("REFERENSI.txt"))))
  print("======================VERDICT=========================")
  print()
  cykParse(token, CNFgrammar)
  print()
  print("======================================================")

if __name__ == "__main__":
  verdict()