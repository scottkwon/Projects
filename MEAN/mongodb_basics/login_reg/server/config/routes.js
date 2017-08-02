const controller = require('../controllers/controller');

module.exports = app => {
    app.get('/', controller.index);
    app.post('/create', controller.create);
    app.post('/login', controller.login);
}