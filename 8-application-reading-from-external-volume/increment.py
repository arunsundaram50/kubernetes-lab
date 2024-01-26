#!/usr/bin/env python3
import os

filename = "/mydata/number.txt"
if not os.path.exists(filename):
  with open(filename, "wt") as fp:
    fp.write("0")

# read number
with open(filename) as fp:
  i = int(fp.read())

# process
i = i+1

# write output
with open(filename, "wt") as fp:
  fp.write(str(i))

if False:
  s = ""
  while s!="quit":
    print("Say something: ", end="")
    s = input()
    print("got "+s)
