#!/usr/bin/node

const args = process.argv;
let prt;
if (args[2] == null) { prt = 'No argument'; } else { prt = args[2]; }
console.log(prt);
