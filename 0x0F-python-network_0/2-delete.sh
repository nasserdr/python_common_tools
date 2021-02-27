#!/bin/bash
# Sends a delete request to the link in first arg
curl -s -XDELETE $1
