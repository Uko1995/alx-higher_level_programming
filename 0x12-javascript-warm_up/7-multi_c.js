#!/usr/bin/node
// Write a script that prints x times “C is fun

const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);
if (isNaN(firstArg)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
