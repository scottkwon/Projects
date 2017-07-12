let express = require('express');
let bodyParser = require('body-parser');
let mongoose = require('mongoose');

let app = express();

app.use(express.static(__dirname+'/static'));
app.use('views', __dirname+'/views');
app.use('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
mongoose.connect('mongodb://localhost/<name_of_db>')

app.get('/', (req,res) => {

})

app.listen(8000, () => {
    console.log('App listening on port 8000')
})