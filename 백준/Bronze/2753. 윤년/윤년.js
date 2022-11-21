var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var A = parseInt(input[0]);

if(A%4==0){
    if(A%400 ==0){console.log("1");}
    else if(A%100 !=0){console.log("1");}
    else{console.log("0");}
}
else{console.log("0");}
