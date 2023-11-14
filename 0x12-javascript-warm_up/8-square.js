#!/usr/bin/node
// Write a script that prints a square

const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('X'.repeat(firstArg));
  }
}
