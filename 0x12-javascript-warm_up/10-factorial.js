#!/usr/bin/node
// Write a script that computes and prints a factorial

const args = process.argv[2];
function factorial (a) {
  if (a <= 1 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(Number(args)));
