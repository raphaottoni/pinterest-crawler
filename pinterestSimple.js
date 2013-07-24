var args = require('system').args;
var page = require('webpage').create();

// Find the address given as parameter
var address = '';
args.forEach(function(arg, i) {
 if(i == 1) {
   address = arg;
 }  
});

//Collect the page data
page.open(address, function () {
       console.log(page.content);  
       phantom.exit();
});

