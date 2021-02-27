#!/bin/bash
# Check content length
curl -sI $1 | gawk -v IGNORECASE=1 '/^Content-Length/ { print $2 }'
