var args = require('system').args;
var page = require('webpage').create();
var page2 = require('webpage').create();
var fs = require('fs');
var content;

// Find the address given as parameter
var address = '';
var nPins   = '';
args.forEach(function(arg, i) {
 if(i == 1) {
   address = arg;
 }else if( i == 2 ) {
        nPins = arg
 }    
});


// Count how many boards are in the page
var countItens = function(){
    var count = page.content.match(/\<div class="item " /g);
    return (count.length);
}


//Collect the page data
page.open(address, function () {

 window.setInterval(function() {
     if(nPins > countItens()) {
      // console.log(window.document.body.scrollTop);
       page.evaluate(function() {
         window.document.body.scrollTop = document.body.scrollHeight;
       });
     }
     else {
       console.log(page.content);  
       phantom.exit();
     }
 }, 500);

});

