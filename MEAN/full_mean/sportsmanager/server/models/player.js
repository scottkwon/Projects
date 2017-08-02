const mongoose = require('mongoose');

const Schema = mongoose.Schema;

let PlayerSchema = new Schema({
    name: {type: String, required:true},
    position: {type: String},
    g1: {type:String, default:"Undecided"},
    g2: {type:String, default:"Undecided"},
    g3: {type:String, default:"Undecided"}
}, {timestamps:true});

mongoose.model('Player', PlayerSchema);