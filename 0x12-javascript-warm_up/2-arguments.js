#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed
let howMany = process.argv.length;
if (howMany === 2) {
    console.log('No argument');
}
else if (howMany === 3) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}
