#!/usr/bin/python

import argparse
from random import randrange

parser = argparse.ArgumentParser(description='fetches any number of words from a wordlist')
parser.add_argument('filename', help='the name of a wordlist you want to fetch from')
parser.add_argument('-c','--count', type=int, default=1,
                    help='the number of words you wish to fetch from the wordlist')
parser.add_argument('-o','--output', help='directs the output to a name of your choice')
args = parser.parse_args()

try:
    with open(args.filename, 'r') as data:
        wordlist = [] 
        while line := data.readline().replace('\n','').strip():
            wordlist.append(str(line))
    
        if args.count > len(wordlist):
            print(f"\n!! The wordlist you have entered doesn't have {args.count} entries therefore the max number of entries in the wordlist will be presented !!")
            args.count = len(wordlist)
            
        if args.output is None:
            print('')
            for x in range(args.count):
                idx = randrange(len(wordlist))
                print(f"{x+1:03}. {wordlist[idx]}")
                wordlist.pop(idx)
            print('')
        else:
            with open(args.output, 'w') as output_file:
                for x in range(args.count):
                    idx = randrange(len(wordlist))
                    output_file.write("%s\n" % wordlist[idx])
                    wordlist.pop(idx)

except Exception as err:
    print("\n\n!! Something went wrong !!\n\n"
          + f"{type(err)=}\n{err=}\n\n")
