#!/usr/bin/node
const fis = require('fs');
fis.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
