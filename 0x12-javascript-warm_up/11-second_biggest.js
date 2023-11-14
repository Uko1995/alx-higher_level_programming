#!/usr/bin/node
// Write a script that searches the second biggest integer the list of arguments

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args.sort().reverse()[1]);
}
