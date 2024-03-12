#!/usr/bin/node

const args = process.argv;
const len = args.length;
if (len <= 3) {
  console.log(0);
} else {
  args.map(Number).slice(2, len).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
