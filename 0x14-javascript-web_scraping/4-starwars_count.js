#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let num = 0;
    for (const result of results) {
      if (result.characters.find((act) => act.endsWith('/18/'))) {
        num += 1;
      }
    }
    console.log(num);
  }
});
