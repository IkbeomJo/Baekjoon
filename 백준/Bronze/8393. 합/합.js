var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var A = parseInt(input[0]);
var result = 0;
for(var i = 1 ; i <= A ; i++){
    result += i;
}
console.log(result);