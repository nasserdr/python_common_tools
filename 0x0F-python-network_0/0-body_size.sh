#!/bin/bash
# Check content length
curl -sI $1 | grep Content-Length | cut -c 17-
