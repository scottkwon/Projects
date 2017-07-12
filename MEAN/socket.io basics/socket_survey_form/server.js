var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(express.static(__dirname+'/static'));
app.use(bodyParser.urlencoded({extended:true}));

app.set('views', __dirname+'/views');
app.set('view engine', 'ejs');

app.get('/', (req,res) => {
    res.render('survey');
})

var server = app.listen(8000, (req,res) => {
    console.log('Server listening on port 8000');
});

var io = require('socket.io').listen(server);

io.sockets.on('connection', (socket) => {
    console.log(socket.id);

    socket.on('post_data', (data) => {
        var flash = "You have submitted the following information to the server: " + JSON.stringify(data) + " Your lucky number emitted by the server is "+ (Math.floor(Math.random()*1000)+1)
        socket.emit('flash_message', flash)
    })

})