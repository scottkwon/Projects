const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const session = require('express-session');
const app = express();

app.use(session({secret: "1xiueqiruncweirybwiuerybc2783"}));
app.use(express.static(__dirname+'/public/dist'));

app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json());

require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);

app.all('*', (req,res,next) => {
    res.sendfile(path.resolve('./public/dist/index.html'));
});

app.listen(8000, () => {
console.log('Listening on port 8000');
})