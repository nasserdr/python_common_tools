#!/bin/bash
# Send a header
curl -s $1 -X POST -d  "email=hr@holbertonschool.com&Subject=I will always be here for PLD"; echo ""
