const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');


var A = parseInt(inputData[0]);
var B = parseInt(inputData[1]);
console.log(A-B);