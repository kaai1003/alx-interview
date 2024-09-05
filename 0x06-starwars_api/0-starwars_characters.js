#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  request(url, async (err, response, body) => {
    if (err) {
      throw err;
    } else {
      body = JSON.parse(body);
      const chars = body.characters;
      for (const char of chars) {
        await new Promise((resolve, reject) => {
          request(char, function (err, response, body) {
            if (err) {
              reject(err);
            } else {
              body = JSON.parse(body);
              console.log(body.name);
              resolve();
            }
          });
        });
      }
    }
  });
}
