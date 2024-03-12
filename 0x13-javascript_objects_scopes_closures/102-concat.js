#!/usr/bin/node

const fs = require('fs');
const fsf = fs.readFileSync(process.argv[2], 'utf8');
const ssf = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fsf + ssf);
