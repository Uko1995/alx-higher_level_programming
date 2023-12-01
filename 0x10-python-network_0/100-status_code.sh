#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
# curl -sI -o /dev/null  "$1" -w "%{http_code}"
curl -w "http_code" "$1"
