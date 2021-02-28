#!/bin/bash
# Display the body only if it has a "200" response
if [ $(curl -s -X GET 0.0.0.0:5000/route_1 -o /dev/null -w %{http_code}) -eq 200 ]; then curl -sb 0.0.0.0:5000/route_1; fi; 
