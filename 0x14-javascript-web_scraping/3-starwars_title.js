#!/usr/bin/node
/*  a script that prints the title of a Star Wars movie
where the episode number matches a given integer */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (errorId, response, body) {
  if (errorId) {
    console.log(errorId);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
