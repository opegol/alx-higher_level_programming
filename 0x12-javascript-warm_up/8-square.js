#!/usr/bin/node

const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i += 1) { console.log(`${'X'.repeat(n)}`); }
}
