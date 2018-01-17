#!/user/bin/env python3

import argparse
import sys
import urllib.request as req
import re
import os
import subprocess as sub

def makeDirectory(dir):
    if not os.path.exists(dir):  # Caution, this is not thread safe!
        os.makedirs(dir)

def execute(allMatches, allOutputMatches, probLetter, magicNum):

    cd = os.path.join(os.getcwd() + "/" + magicNum + "/", probLetter + ".py")
    #sub.call(['chmod', '+x', cd])
    print("\n======= Problem " + probLetter + " =========")
    index = 0

    for match in allMatches:
        input = ""
        for line in match:
            input += line + "\n"
        p = sub.run(['python3', cd], stdout=sub.PIPE, input=input, encoding="utf-8")
        p.stdout = p.stdout[:-1]
        if str(p.stdout) == str(allOutputMatches[index]):
            print("PASSED")
        else:
            print("*FAILED* expected: " + allOutputMatches[index] + " actual: " + p.stdout + "\n")
        index += 1

    print()



if __name__ == "__main__":

    if len(sys.argv) == 0:
        magicNum = "911"
        probLetter = "A"
    elif len(sys.argv) == 3:
        magicNum = sys.argv[1]
        probLetter = sys.argv[2]
    else:
        print("\nPlease input a contest number and a problem letter\n")

    link = "http://codeforces.com/contest/" + magicNum + "/problem/" + probLetter
    f = req.urlopen(link)
    file = f.read()

    inputPattern = re.compile("Input<\/div><pre>([^<]*)<br \/>([^<]*)")
    allInputMatches = inputPattern.findall(str(file))
    outputPattern = re.compile("Output<\/div><pre>([^<]*)<br")
    allOutputMatches = outputPattern.findall(str(file))

    directory = "/Users/mckade/PycharmProjects/hackerRank/" + magicNum
    makeDirectory(directory)

    execute(allInputMatches, allOutputMatches, probLetter, magicNum)












