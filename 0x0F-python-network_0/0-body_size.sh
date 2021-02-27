#!/bin/bash
# Check content length
curl -sI $1 | awk -v IGNORECASE=1 '/Content-Length/ { print $2 }'
