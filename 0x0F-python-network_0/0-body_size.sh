#!/bin/bash
# Check content length
curl -o /dev/null -s -w "%{size_download}\n" $1
