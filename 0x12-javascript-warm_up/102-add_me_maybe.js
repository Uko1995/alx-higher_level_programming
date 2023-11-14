#!/usr/bin/node
// function increments and calls another function

module.exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
