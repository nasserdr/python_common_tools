#!/bin/bash
# Display the body only if it has a "200" response
curl -o /dev/null -s -w %{http_code} $1
