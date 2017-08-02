const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(express.static(__dirname+'/static'));
app.use(bodyParser.urlencoded({extended:true}));
app.set('views', __dirname+'/views');
app.set('view engine', 'ejs');

require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);

app.listen(8000, () => {
    console.log('Listening on port 8000');
});