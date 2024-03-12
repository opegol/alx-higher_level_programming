#!/usr/bin/node

const n = Math.floor(Number(process.argv[2]));
let prt;
if (isNaN(n)) { prt = 'Not a number'; } else { prt = `My number: ${n}`; }
console.log(prt);
