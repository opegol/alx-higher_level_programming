#!/usr/bin/node
const fis = require('fs');
fis.writeFile(process.argv[2], process.argv[3], (error) => {
  if (error) console.log(error);
});
