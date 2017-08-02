let controller = require('../controllers/controller');
module.exports = (app) => {
    app.get('/api/notes', controller.index);
    app.post('/api/notes', controller.create);

    app.all('*', (req,res,next) => {
        res.sendfile(path.resolve('./public/dist/index.html'));
    });
}