
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


//set timeout 
window.setTimeout(function () {
                console.log('HTML-Error-Code: ' + "666");
                phantom.exit();
            }, 10000);

//Collect the page data
page.open(address, function (resource) {

  //verify if the timeline content was generated
  var myReg = new RegExp('class="commentDescriptionTimeAgo"');
  timeAgo = myReg.exec(page.content);
  if (timeAgo == null) { return; }
    
  console.log(page.content);
  phantom.exit();

});

page.onResourceReceived = function(resource) {
  if(resource.url === address && resource.status != '200') {
    //console.log('Url: ' + resource.url);
    console.log('HTML-Error-Code: ' + resource.status);
    phantom.exit();
  }
}
