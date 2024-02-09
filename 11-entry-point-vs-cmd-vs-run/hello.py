#!/usr/bin/env python3
import os, sys

name = str(os.getenv("name"))
print("Hello, "+name)

for arg in sys.argv:
  print(arg)
