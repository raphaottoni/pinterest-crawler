var args = require('system').args;
var page = require('webpage').create();
var fs = require('fs');

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
  //console.log(count.length);
  if (count) { return count.length;} 
  return 0
}

//set timeout 
window.setTimeout(function () {
                console.log('HTML-Error-Code: ' + "666");
                phantom.exit();
            }, 60000);


//Collect the page data
page.open(address, function (resource) {

  //Find how many boards the user has
  var myReg = new RegExp('name="pinterestapp:boards" content="(.*)" ');
  nBoards= myReg.exec(page.content);
  if (nBoards == null) { return; }
  nBoards = nBoards[1]
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

page.onResourceReceived = function(resource) {
  if(resource.url === address && resource.status != '200') {
    //console.log('Url: ' + resource.url);
    console.log('HTML-Error-Code: ' + resource.status);
    phantom.exit();
  }
}
