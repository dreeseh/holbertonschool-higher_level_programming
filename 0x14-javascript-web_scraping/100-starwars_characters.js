#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    for (const key in JSON.parse(body).characters) {
      request.get(JSON.parse(body).characters[key], (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
