#!/usr/bin/node
// a script that prints x times “C is fun”

let x = process.argv[2];
if (isNaN(x)) {
    console.log('Missing number of occurrences');
}
else {
    for (let count = 0 ; count <= x - 1 ; count++) {
	console.log('C is fun');
    }
}
