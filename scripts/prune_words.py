#!/usr/bin/python

import sys, getopt

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hi:o:l:",["ifile=","ofile=","letters="])
  except getopt.GetoptError:
    print('prune_words.py -i <inputfile> -o <outputfile> -l <num letters to keep>')
    sys.exit(2)

  inputfile = ''
  outputfile = ''
  count = 0
  for opt, arg in opts:
    if opt == '-h':
      print('prune_words.py -i <inputfile> -o <outputfile> -l <num letters to keep>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
    elif opt in ("-l", "--letters"):
      count = int(arg)

  if inputfile == '' or outputfile == '' or count == 0:
    print('Missing arguments: prune_words.py -i <inputfile> -o <outputfile> -l <num letters to keep>')
    sys.exit()


  fout = open(outputfile, 'w')

  with open(inputfile) as fin:
    for line in fin:
      if len(line.strip()) == count:
        fout.write(line)


if __name__ == "__main__":
    main(sys.argv[1:])