#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user
id and computes a dictionary of user ids by occurrence */

const dict = require('./101-data.js').dict;

const reesesDict = {};
for (const k in dict) {
  reesesDict[dict[k]] = [];
}

for (const k in dict) {
  reesesDict[dict[k]].push(k);
}

console.log(reesesDict);
