#!/usr/bin/env python3
import os

name = str(os.getenv("name"))
greeting = str(os.getenv("greeting"))
print(greeting+", "+name)
