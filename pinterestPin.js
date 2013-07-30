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

    if (count){ return (count.length);}
    return 0
}



//set timeout 
window.setTimeout(function () {
                console.log('HTML-Error-Code: ' + "666");
                phantom.exit();
            }, 30000);

//Collect the page data
page.open(address, function () {

 //check if it is a html of a board
 var myReg = new RegExp('<span class="buttonText">Follow Board</span>');
 isBoardPage= myReg.exec(page.content);
 if (isBoardPage == null) { return; }

 window.setInterval(function() {
     itens = countItens();
     if(nPins > itens  && itens % 25 == 0) {
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

page.onResourceReceived = function(resource) {
  if(resource.url === address && resource.status != '200') {
    //console.log('Url: ' + resource.url);
    console.log('HTML-Error-Code: ' + resource.status);
    phantom.exit();
  }
}
