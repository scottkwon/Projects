const mongoose = require('mongoose');

const Schema = mongoose.Schema;

let personSchema = new Schema({
    name: {type: String, required:true}
}, {timestamps:true});

mongoose.model('Person', personSchema);