#!/usr/bin/node
// a script that prints 3 lines:
// (like 1-multi_languages.js)
// but by using an array of string and a loop

const theLines = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let step = 0 ; step < theLines.length ; step++) {
    console.log(theLines[step]);
}
