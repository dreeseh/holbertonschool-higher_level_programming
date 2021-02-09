#!/usr/bin/node
// a script that display the status code of a GET request

const url = process.argv[2];
const request = require('request');

request(url, 'utf-8', function (errorObj, request, body) {
  if (errorObj) {
    console.log(errorObj);
  } else {
    console.log('code: ' + request.statusCode);
  }
});
