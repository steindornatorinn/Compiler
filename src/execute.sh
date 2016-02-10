#!/bin/bash
Program = $1
python compiler < Program > program.code
python interpreter < program.code
