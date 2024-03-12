#!/usr/bin/node

const n = process.argv.length;
let prt;
if (n === 2) { prt = 'No argument'; } else if (n > 2) { prt = 'Argument found'; }
console.log(prt);
