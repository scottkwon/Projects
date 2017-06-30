//requires the http module
var http = require('http');
//requires the file system (read/write) module
var fs = require('fs');
//create server
var server = http.createServer(function(request,response){
    //log the url the client is requesting
    console.log('client request URL:', request.url);
    //routing
    if(request.url === '/car'){
        fs.readFile('./views/cars.html', 'utf8', function(errors,contents){
            response.writeHead(200,{'Content-Type':'text/html'}); //send some data about response
            response.write(contents); //send body of response
            response.end(); //finished
        });
    }
    else if(request.url === '/images/car.png'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/car.png', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/png'});
          response.write(contents);
          response.end();
        });
      }
    else if (request.url === '/cat') {
        fs.readFile('./views/cats.html', 'utf8', function(errors,contents){
            response.writeHead(200,{'Content-Type':'text/html'}); //send some data about response
            response.write(contents); //send body of response
            response.end(); //finished
        });
    }
    else if(request.url === '/images/cat.png'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/cat.png', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/png'});
          response.write(contents);
          response.end();
      });
  }
    else if (request.url === '/cars/new') {
        fs.readFile('./views/newcar.html', 'utf8', function(errors,contents){
            response.writeHead(200,{'Content-Type':'text/html'}); //send some data about response
            response.write(contents); //send body of response
            response.end(); //finished
        });
    }
    else{
        response.writeHead(404);
        response.end('URL not found!!');
    }
});
//server port
server.listen(8000);
// print to terminal
console.log('Running in localhost:8000')
