#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
curl -sI -w "%{http_code}" "$1"
