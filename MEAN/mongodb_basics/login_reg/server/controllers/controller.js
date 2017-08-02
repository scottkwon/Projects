const bcrypt = require('bcryptjs');
const mongoose = require('mongoose');
const User = mongoose.model('User');

module.exports = {
    index: (req,res) => {
        res.render('login');
    },

    create: (req,res) => {
        let newUser = new User(req.body);
        newUser.save( (newUserErr, newUser) => {
            if (newUserErr){
                res.render('login', {errors: newUserErr.errors});
            } else {
                res.json(newUser);
            };
        });
    },

    login: (req,res) => {
        User.findOne({email: req.body.email}, (findErr,user) => {
            if(findErr){
                console.log(findErr);
                res.redirect('/')
            } else {
                if(bcrypt.compareSync(req.body.password, user.password)){
                    res.json(user)
                } else {
                    console.log("Invalid password");
                };
            };
        });
    },
}