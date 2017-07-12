var express = require("express");
var session = require("express-session")


var app = express();

app.set('views', __dirname + "/views");
app.set('view engine', 'ejs');

app.use(session({secret: 'a'}));


app.get('/', (req,res) => {

    if (!req.session.count){
        req.session.count = 0;
    };

    req.session.count += 1;
    
    res.render('index', {count: req.session.count});
})

app.post('/add2', (req,res) => {
    req.session.count+=1;
    res.redirect('/')
})

app.post('/reset', (req,res) => {
    req.session.count = 0;
    res.redirect('/')
})

app.listen(8000, () => {
    console.log("Listening on port 8000")
})