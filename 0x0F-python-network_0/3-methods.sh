#!/bin/bash
# Sends a delete request to the link in first arg
curl -sI $1 | grep Allow | cut -c 8-
