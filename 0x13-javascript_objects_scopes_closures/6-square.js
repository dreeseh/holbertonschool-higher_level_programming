#!/usr/bin/node
/* a class Square that defines a square and
inherits from Rectangle of 4-rectangle.js */

const baseSquare = require('./5-square');

class Square extends baseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
