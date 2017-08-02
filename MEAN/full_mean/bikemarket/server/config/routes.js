const user = require('../controllers/usercontroller');

module.exports = app => {
    app.get('/api/users', user.getUsers);
    app.post('/api/users/register', user.register);
    app.post('/api/users/login', user.login);
}