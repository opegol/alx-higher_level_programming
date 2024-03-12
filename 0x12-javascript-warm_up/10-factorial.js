#!/usr/bin/node

function factorial (i) {
  if (i === 0 || i === 1 || isNaN(i)) {
    return (1);
  } else { return i * factorial(i - 1); }
}
const args = process.argv;
console.log(factorial(Number(args[2])));
