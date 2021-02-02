#!/usr/bin/node
// a function that executes x times a function

exports.callMeMoby = function (x, theFunction) {
  for (let count = 0; count < x; count++) {
    theFunction();
  }
};
