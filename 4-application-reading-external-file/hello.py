#!/usr/bin/env python3

with open("name.txt") as fp:
  name = fp.read()

print("Hello, "+name)
