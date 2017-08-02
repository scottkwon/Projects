const bcrypt = require('bcryptjs');
const mongoose = require('mongoose');
const User = mongoose.model('User');

module.exports = {
    index: (req,res) => {
        res.render('login');
    },

    register: (req,res) => {
        let newUser = new User(req.body);
        newUser.password = bcrypt.hashSync(req.body.password, bcrypt.genSaltSync(8));
        newUser.save( (err, currUser) => {
            if (err){
                console.log(err);
                let errors = [];
                for (let err in currUser.errors){
                    errors.push(currUser.errors[i].message);
                }
                return res.status(400).send(errors)
            }
            if(currUser == null){
                let errors =["Email is already registered!"];
                return res.status(400).send(errors);
            } else {
                res.json(currUser);
                req.session.userid = currUser._id;
            };
        });
    },

    login: (req,res) => {
        User.findOne({email: req.body.email}, (findErr,user) => {
            if(findErr){
                let errors = [];
                for(let i in findErr){
                    errors.push(findErr.errors[i].message)
                }
                return res.status(400).send(errors);
            }
            if(user == null){
                let errors = ["Email not found, please register!"]
                return res.status(400).send(errors)
            }
            if(bcrypt.compareSync(req.body.password, user.password)){
                console.log("In the log-in backend controller");
                req.session.userid = user._id;
                res.json(user);
            } else {
                let errors = ["Invalid credentials!"];
                return res.status(400).send(errors)
            };
        });
    },

    getUsers: (req,res) =>{
        User.find({}, (err, userlist) => {
            if(err){
                let errors = [];
                for(let i in err){
                    errors.push(err.errors[i].message)
                }
                return res.status(400).send(errors)
            } else {
                res.json(userList)
            }
        })
    }
}