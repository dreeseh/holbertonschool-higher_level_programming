#!/usr/bin/node
// a script that imports an array and computes a new array

const list = require('./100-data').list;
const reesesList = list.map((value, index) => value * index);

console.log(list);
console.log(reesesList);
