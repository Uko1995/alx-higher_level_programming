#!/usr/bin/node
// get the status code of GET request

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${response.statusCode}`);
});
