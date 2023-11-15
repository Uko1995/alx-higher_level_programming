#!/usr/bin/node
// write a class with constructor

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // print the rectangle using the letter "X"
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    // doubles the width and height
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    // rotates the value of the width and height
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}

class Square extends Rectangle {
  // square class inherits from rectangle class
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
