var args = require('system').args;
var page = require('webpage').create();

// Find the address given as parameter
var address = '';
args.forEach(function(arg, i) {
 if(i == 1) {
   address = arg;
 }
});


// Count how many boards are in the page
var countItens = function(){   

 var count = page.content.match(/\<div class="item "\>/g);
 console.log(count.length);
 return (count.length);
}

//Collect the page data
page.open(address, function () {

 //Find how many boards the user has
 var myReg = new RegExp('name="pinterestapp:boards" content="(.*)" ');
 //console.log(myReg.exec(page.content)[1]);
 nBoards= myReg.exec(page.content)[1];

 window.setInterval(function() {
     if(nBoards > countItens()) {
       console.log(window.document.body.scrollTop);
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
