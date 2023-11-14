#!/usr/bin/node
// Write a function that executes x times a function

module.exports.callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
