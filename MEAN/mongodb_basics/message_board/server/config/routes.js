const controller = require('./../controllers/controller.js');

module.exports = app => {
    app.get('/', controller.index);
    app.post('/posts', controller.createPost);
    app.post('/comments/:post_id', controller.createComment);
}