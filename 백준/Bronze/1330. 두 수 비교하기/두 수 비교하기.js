var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');

var A = parseInt(input[0]);
var B = parseInt(input[1]);

if(A>B){console.log(`>`);}
else if(A<B){console.log(`<`);}
else if(A==B){console.log(`==`);}