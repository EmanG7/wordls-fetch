# wordls-fetch
 
"wordls-fetch" randomly fetches words from a wordlist like common.txt or rockyou.txt to give variety to crackable password in vulnerable environments.

By default, it grabs one word randomly from the wordlist but using "-c" or "--count" you can get any unique entries from the wordlist as you like.

## help page
```
usage: wordls-fetch.py [-h] [-c COUNT] [-o OUTPUT] filename

fetches any number of words from a wordlist

positional arguments:
  filename              the name of a wordlist you want to fetch from

options:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        the number of words you wish to fetch from the wordlist
  -o OUTPUT, --output OUTPUT
                        directs the output to a name of your choice
```

## example
> python wordls-fetch.py /usr/share/wordlists/rockyou.txt -c 5
or
> wordls-fetch -c 3 /usr/share/wordlists/rockyou.txt
