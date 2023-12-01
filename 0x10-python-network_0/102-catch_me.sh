#!/usr/bin/bash
# Bash script that makes a request and causes server to respond with a request

curl -X POST 0.0.0.0:5000/catch_me -d "you_got_me" -o /dev/null
