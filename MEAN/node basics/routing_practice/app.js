//requires the http module
var http = require('http');
//requires the file system (read/write) module
var fs = require('fs');
//create server
var server = http.createServer(function(request,response){
    //log the url the client is requesting
    console.log('client request URL:', request.url);
    //routing
    if(request.url === '/'){
        fs.readFile('index.html', 'utf8', function(errors,contents){
            response.writeHead(200,{'Content-Type':'text/html'}); //send some data about response
            response.write(contents); //send body of response
            response.end(); //finished
        });
    } else if (request.url === '/ninjas') {
        fs.readFile('ninjas.html', 'utf8', function(errors,contents){
            response.writeHead(200,{'Content-Type':'text/html'}); //send some data about response
            response.write(contents); //send body of response
            response.end(); //finished
        });
    } else if (request.url === '/dojos/new') {
        fs.readFile('dojos.html', 'utf8', function(errors,contents){
            response.writeHead(200,{'Content-Type':'text/html'}); //send some data about response
            response.write(contents); //send body of response
            response.end(); //finished
        });
    } else{
        response.writeHead(404);
        response.end('URL not found!!')
    }
});
//server port
server.listen(8000);
// print to terminal
console.log('Running in localhost:8000')
