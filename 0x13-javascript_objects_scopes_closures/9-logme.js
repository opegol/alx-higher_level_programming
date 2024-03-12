#!/usr/bin/node

let prt = 0;
exports.logMe = function (item) {
  console.log(`${prt++}: ${item}`);
};
