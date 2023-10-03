#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
curl -sX GET -H "X-School-User-Id: 98" "$1"
