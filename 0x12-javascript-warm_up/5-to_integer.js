#!/usr/bin/node
/*
Write a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/

const args = process.argv.slice(2);
const firstArg = parseInt(args[0]);
if (!isNaN(firstArg)) {
  console.log('My number: ' + firstArg);
} else {
  console.log('Not a number');
}
