const mongoose = require('mongoose');

const Person = mongoose.model('Person');

module.exports = {
    showAll: (req,res) => {
        Person.find({}, (err,people) => {
            if(err){
                console.log(err);
            } else {
                res.json(people);
            };
        });
    },

    add: (req,res) => {
        let newGuy = new Person({name: req.params.name});
        newGuy.save( (err, savedGuy) => {
            if(err){
                console.log("Cannot add the new guy");
            } else {
                console.log(savedGuy);
                res.redirect('/')
            };
        });
    },

    remove: (req,res) => {
        Person.findOne({name: req.params.name}, (err, person) => {
            if(err){
                console.log("Person cannot be found to delete");
            } else {
                person.remove()
                res.redirect('/')
            }
        })
    },

    showUser: (req,res) => {
        Person.findOne({name: req.params.name}, (err,person) => {
            if(err){
                console.log("Cannot find user show page");
            } else {
                res.json(person)
            }
        })
    }
}