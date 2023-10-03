#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
curl -sX POST -d @"$2" -H "Content-Type: application/json" "$1"
