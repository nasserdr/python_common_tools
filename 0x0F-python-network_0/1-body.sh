#!/bin/bash
# Display the body only if it has a "200" response
curl -sI $1 | grep 200
