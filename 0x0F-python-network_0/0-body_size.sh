#!/usr/bash
URL= $0
curl -sI $URL | grep -i Content-Length
