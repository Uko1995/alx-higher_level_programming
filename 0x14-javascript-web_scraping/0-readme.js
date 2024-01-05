#!/usr/bin/node
// read and print out contents of a file

const fs = require('fs');
const filePath = process.argv[2];

if (!filePath) {
  console.log('Enter a valid file path');
}

try {
  const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
}
