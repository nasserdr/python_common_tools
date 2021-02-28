#!/bin/bash
# Post json content
curl -H "Content-Type: application/json" -X POST -d $2 $1
