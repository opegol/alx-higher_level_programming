#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const characterUrl of characters) {
      req(characterUrl, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
