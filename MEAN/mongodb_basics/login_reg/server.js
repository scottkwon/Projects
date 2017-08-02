const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(express.static(__dirname+'/client/static'));
app.set('views', __dirname + '/client/views');
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);

app.listen(8000, () => {
console.log('Listening on port 8000');
})