#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
curl -sI "$1" | grep -i "allow" | cut -d " " -f2-
