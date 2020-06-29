#!/bin/env python 

import argparse
import re
in_users = []

my_parser = argparse.ArgumentParser()

my_parser.add_argument('in_file', help='Text file containing users')

my_parser.add_argument('out_file', help='Output destination')

args = my_parser.parse_args()

in_file = args.in_file
out_file = args.out_file

f = open(in_file, "r")

for x in f:
    in_users.append(x)

c = open(out_file,"a")
for x in in_users:
    c.write((re.findall(r'\[(.*?)\]', x))[0] + "\n")

c.close()
    
print('You can find the list of users at ' + out_file)
