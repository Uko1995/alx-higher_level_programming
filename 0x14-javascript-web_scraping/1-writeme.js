#!/usr/bin/node
// writes to a file

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath) {
  console.log('Enter a valid file path');
}

try {
  fs.writeFileSync(filePath, content, 'utf-8');
} catch (err) {
  console.error(err);
}
