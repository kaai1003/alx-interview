#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  request(url, function (err, response, body) {
    if (!err) {
      body = JSON.parse(body);
      const chars = body.characters;
      chars.forEach((char) => {
        request(char, function (err, response, body) {
          if (!err) {
            body = JSON.parse(body);
            console.log(body.name);
          }
        });
      });
    }
  });
}
