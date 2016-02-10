#!/bin/bash
Program=$1
python compiler.py < $Program > program.code
python interpreter.py < program.code
