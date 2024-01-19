#!/usr/bin/env python3

with open("number.txt") as fp:
  i = int(fp.read())
  i = i+1

with open("number.txt", "wt") as fp:
  fp.write(str(i))

s = ""
while s!="quit":
  print("Say something: ", end="")
  s = input()
  print("got "+s)
