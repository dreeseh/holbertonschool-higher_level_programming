#!/usr/bin/node
//  a script that prints the addition of 2 integers

const numberOne = parseInt(process.argv[2]);
const numberTwo = parseInt(process.argv[3]);

function add(numberOne, numberTwo) {
    console.log(numberOne + numberTwo);
}
add(numberOne, numberTwo);
