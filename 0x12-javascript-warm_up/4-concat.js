#!/usr/bin/node

// Write a script that prints two arguments passed to it

const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
