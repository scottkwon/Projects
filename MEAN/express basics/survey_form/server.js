var express = require('express');
var bodyParser = require('body-parser');
var session = require('express-session')

var app = express();

app.use(express.static(__dirname+ '/static'));
app.use(bodyParser.urlencoded({extended:true}));

app.set('views', __dirname + '/views')
app.set('view engine', 'ejs')

app.use(session({secret:'13i4u1qu3yehqupwehdqrfwer'}))

app.get('/', (req,res) => {
    res.render('index');
})

app.post('/process', (req,res) => {
    req.session.name = req.body.name
    req.session.location = req.body.location
    req.session.lang = req.body.lang
    req.session.comment = req.body.comment 

    res.redirect('/result')
})

app.get('/result', (req,res) => {

    context = {
        'name': req.session.name,
        location: req.session.location,
        lang: req.session.lang,
        comment: req.session.comment
    }

    res.render('result', context)
})

app.listen(8000, (req,res) => {
    console.log('Listening on port 8k')
})