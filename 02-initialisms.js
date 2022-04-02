'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'InitialismConverter' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function InitialismConverter(s) {
    // Write your code here
    const re = /[^A-Z ]/g;
    s = s.replace(re, '');
    console.log(s);
    s = s.replace(/\s+/g, ' ');
    console.log(s);
    s = s.split(' ');
    console.log(s);
    let y = '';
    for (const x of s) {
        if (x && x[0] === x[0].toUpperCase())
            y += x[0];
    }
    return y;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const result = InitialismConverter(s);

    ws.write(result + '\n');

    ws.end();
}
