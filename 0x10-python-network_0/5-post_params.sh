#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
