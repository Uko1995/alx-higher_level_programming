#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
