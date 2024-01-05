#!/usr/bin/node
// writes to a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (!filePath) {
    console.log('Enter a valid file path');
  }

  try {
    fs.writeFileSync(filePath, body, 'utf-8');
  } catch (err) {
    console.error(err);
  }
});
