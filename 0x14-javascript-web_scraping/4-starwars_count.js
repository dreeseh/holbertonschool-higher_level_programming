#!/usr/bin/node
/* a script that prints the number of movies
where the character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];
let theCounter = 0;

request(url, function (errorObj, response, body) {
  if (errorObj) {
    console.log(errorObj);
  } else {
    let numOfMovies = JSON.parse(body).results;
    for (let i = 0; i < numOfMovies.length; i++) {
      for (let j = 0; j < numOfMovies[i].characters.length; j++) {
        if (numOfMovies[i].characters[j].search('/18/') > 0) {
          theCounter++;
        }
      }
    }
  }
  console.log(theCounter);
});
