#!/bin/bash
# Display the allowed methods
curl -sI $1 | grep Allow | cut -c 8-
