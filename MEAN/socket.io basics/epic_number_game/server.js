var express = require('express');

var app = express();

app.use(express.static(__dirname+'/static'));

app.set('views', __dirname+'/views');
app.set('view engine', 'ejs');

app.get('/', (req,res) => {
    res.render('index');
});

var server = app.listen(8000, (req,res) => {
    console.log('Server listening on port 8000');
});

var io = require('socket.io').listen(server);

var counter = 0

io.sockets.on('connection', (socket) => {
    console.log(socket.id);
    
    
    socket.on('count_data', (data) => {
        io.emit('count', {
            count: counter++,
        });
    });

    socket.on('reset', (data) => {
        counter = 0
        io.emit('count', {
            count: counter,
        });
    });

});