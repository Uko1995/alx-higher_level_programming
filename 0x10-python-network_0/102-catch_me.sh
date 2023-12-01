#!/usr/bin/bash
# Bash script that makes a request and causes server to respond with a request

curl -sX POST 0.0.0.0:5000/catch_me -w "you_got_me" -o /dev/null
