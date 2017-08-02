let express = require('express');
let bodyParser = require('body-parser');
let mongoose = require('mongoose');

let app = express();

app.use(express.static(__dirname+'/static'));
app.set('views', __dirname+'/views');
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
mongoose.connect('mongodb://localhost/quotes');

var quoteSchema = new mongoose.Schema({
    name: {type: String, required: true},
    quote: {type: String, required: true},
}, {timestamps: true});

mongoose.model('Quote', quoteSchema);
var Quote = mongoose.model('Quote');

require("./server/config/routes.js")(app);

app.listen(8000, ()=>{
    console.log('listening on port 8000');
});

