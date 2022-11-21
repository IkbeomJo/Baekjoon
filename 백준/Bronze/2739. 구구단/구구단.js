var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var A = parseInt(input[0]);

for(var i = 1 ; i<10; i++){
    console.log(`${A} * ${i} = ${A*i}`);
}