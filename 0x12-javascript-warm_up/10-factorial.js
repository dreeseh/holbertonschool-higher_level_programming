#!/usr/bin/node
// a script that computes and prints a factorial

const castAsInt = parseInt(process.argv[2]);

if (castAsInt === undefined || isNaN(castAsInt)) {
    console.log(1);
}
else {
    console.log(factorial(castAsInt));
}

function factorial (i) {
    if (i === 0) {
	return 1;
    }
    else {
	return i * factorial(i - 1);
    }
}
