var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var h = parseInt(input[0]);
var m = parseInt(input[1]);

if(m<45){
    if(h==0){
        h=23;
        m+=15
        console.log(`${h} ${m}`);
    }
    else{
        h-=1;
        m+=15;
        console.log(`${h} ${m}`);
    }
}
else{
    m-=45;
    console.log(`${h} ${m}`);
}