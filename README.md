# The_Fuzzer
A fuzz test program that identifies reflected Cross-Site Scripting (XSS) bugs. 
The script will take in a target url link with its necessary query variable at
the end, and the user will input a string payload. The url link and payload 
will then be linked, at will be checked to see if it visible within the POST 
request.

# Dependencies/libraries used
Two dependencies/libraries were used:
  * requests
      * allows for a particular link to be posted upon request in this script.
  * argparse
      * enables parsing arguments passed through console when running program.
      
# How to run the program
  * Python3 must be installed and must have python libraries requests and
    argparse.
  * In command line, the command needed to run the program is:
      * python3 fuzzer.py -u [URL] -r [FUZZLIST]
          * flags:
              * -h, --help: shows the instructions on how to use fuzzer.py
              * -u: the target url link that will be fuzzed. If this is left 
                    empty, then within the program, user will be asked to input
                    a target url.
              * -r: if the user has a fuzzing wordlist, the path must be 
                    written to the wordlist so contents can be put into a fuzz 
                    list. If user does not have, then the user will have input
                    a single script that they want to use for fuzzing.
