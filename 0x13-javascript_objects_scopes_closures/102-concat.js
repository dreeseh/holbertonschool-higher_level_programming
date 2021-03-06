#!/usr/bin/node
/* a script that imports a dictionary of occurrences by
user id and computes a dictionary of user ids by occurrence */

const fs = require('fs');

const fileA = fs.readFileSync(`./${process.argv[2]}`);
const fileB = fs.readFileSync(`./${process.argv[3]}`);
fs.appendFileSync(`./${process.argv[4]}`, fileA + fileB, 'utf-8');
