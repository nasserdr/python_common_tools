#!/bin/bash
# Check content length
curl -sI $1 | grep -i Content-Length
