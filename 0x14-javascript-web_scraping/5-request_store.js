#!/usr/bin/node
const fis = require('fs');
const req = require('request');
req(process.argv[2]).pipe(fis.createWriteStream(process.argv[3]));
