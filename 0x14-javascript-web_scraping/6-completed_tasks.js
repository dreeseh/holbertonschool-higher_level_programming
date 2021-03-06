#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');
const reesesJSON = {};

request(url, function (errorId, response, body) {
  if (errorId) {
    console.log(errorId);
  } else {
    for (const user of JSON.parse(body)) {
      if (user.completed === true) {
        if (!(user.userId in reesesJSON)) {
          reesesJSON[user.userId] = 1;
        } else {
          reesesJSON[user.userId] = reesesJSON[user.userId] + 1;
        }
      }
    }
  }
  console.log(reesesJSON);
});
