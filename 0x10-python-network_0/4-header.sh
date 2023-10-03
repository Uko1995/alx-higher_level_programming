#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
curl -H "X-School-User-Id=98" "$1"
