var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var A = parseInt(input[0]);
var B = parseInt(input[1]);
var C = parseInt(input[2]);
var result = 0;
var maxV = 0;
if(A == B && A == C){
    result = 10000 + A * 1000;
}
else if(A==B || B==C || A==C){
    if(A == B){
        result = 1000 + A * 100;
    }
    else{
        result = 1000 + C * 100; 
    }
}
else{
    A > B ? (A > C ? maxV=A : maxV=C) : (B > C ? maxV=B : maxV=C);
    result = maxV*100;
}
console.log(result);