#!/usr/bash
URL= $1
curl -sI $URL | grep -i Content-Length
